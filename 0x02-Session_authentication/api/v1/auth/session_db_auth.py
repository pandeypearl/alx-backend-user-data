#!/usr/bin/env python3
"""
SessionDBAuth module
"""

from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession
from datetime import datetime, timedelta
from flask import request


class SessionDBAuth(SessionExpAuth):
    """
    Inherits from SessionExpAuth
    """

    def create_session(self, user_id=None):
        """
        creates and stores new instance of UserSession
        and returns the Session ID
        """
        if not user_id:
            return None
        session_id = super().create_session(user_id)
        if not session_id:
            return None
        session_data = {"user_id": user_id, "session_id": session_id}
        obj = UserSession(**session_data)
        obj.save()
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """
        Returns the User ID by requesting UserSession
        in the database based on session_id
        """
        if not session_id:
            return None
        try:
            UserSession.load_from_file()
            objs = UserSession.search({"session_id": session_id})
            if not objs or len(objs) == 0:
                return None
            date_limit = (timedelta(seconds=self.session_duration) +
                          objs[0].created_at)
            if date_limit < datetime.now():
                return None
            return objs[0].user_id
        except Exception as e:
            return None

    def destroy_session(self, request=None):
        """
        Destroys the UserSession based on the
        Session ID from the request cookie
        """
        if not request:
            return False
        try:
            session_id = self.session_cookie(request)
            if not session_id:
                return False
            objs = UserSession.search({"session_id": session_id})
            del self.user_id_by_session_id[session_id]
            if objs and len(objs) > 0:
                objs[0].remove()
                return True
        except Exception as e:
            return False
