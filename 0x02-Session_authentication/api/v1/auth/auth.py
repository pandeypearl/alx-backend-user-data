#!/usr/bin/env python3
"""
Defining Auth Class
"""

from flask import request
from typing import TypeVar, List
from tabnanny import check
import os

User = TypeVar('User')


class Auth:
    """
    Class managing API authentication.
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Returns false - path and excluded_paths
        """
        check = path
        if path is None or excluded_paths is None or excluded_paths == []:
            return True
        if path in excluded_paths:
            return False
        if path[-1] == '/' and path[:-1] in excluded_paths:
            return False
        if path[-1] != '/' and path + '/' in excluded_paths:
            return False
        for exp in excluded_paths:
            if exp[-1] == "*" and path.startswith(exp[:-1]):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        Returns None - request
        """
        if request is None or "Authorization" not in request.headers:
            return None
        return request.headers["Authorization"]

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns None - request
        """
        return None

    def session_cookie(self, request=None):
        """
        Returns a cookie value from a request
        """
        if not request:
            return None
        cookie_name = os.getenv("SESSION_NAME")
        return request.cookies.get(cookie_name)
