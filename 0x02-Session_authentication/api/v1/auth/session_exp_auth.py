#!/usr/bin/env python3
"""
SessionExpAuth module
"""

from api.v1.auth.session_auth import SessionAuth
import os
from datetime import datetime, timedelta


class SessionExpAuth(SessionAuth):
    """
    Inherits from SessionAuth
    Adds expiration date to session Id
    """

    def __init__(self):
        """
        Constructor function
        """
        duration = os.getenv('SESSION_DURATION')
        try:
            if not duration:
                self.session_duration = 0
            else:
                self.session_duration = int(duration)
        except Exception as e:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """
        Creating a session
        """
        session_id = super().create_session(user_id)
        if not session_id:
            return None
        session_directory = {
            "user_id": user_id,
            "created_at": datetime.now()
        }
        self.user_id_by_session_id[session_id] = session_directory
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """
        Returns user_id from the session dictionary
        """
        if not session_id or session_id not in self.user_id_by_session_id:
            return None
        if self.session_duration <= 0:
            return self.user_id_by_sesssion_id[session_id]["user_id"]
        if "created_at" not in self.user_id_by_session_id["session_id"]:
            return None
        date_limit = (timedelta(seconds=self.session_duration) +
                      self.user_id_by_session_id[session_id]["created_at"])
        if date_limit < datetime.now():
            return None
        return self.user_id_by_session_id[session_id]["user_id"]
