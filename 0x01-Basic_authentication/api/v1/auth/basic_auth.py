#!/usr/bin/env python3
"""
Basic Auth Module inherits from Auth
"""

from api.v1.auth.auth import Auth
import base64
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    """
    Inherits from Auth Moodule
    """
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """
        Returns ase64 part of the Authorization header for a Basic Authentication
        """
        if (
           not authorization_header or
           not isinstance(authorization_header, str) or
           not authorization_header.startswith("Basic ")):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """
        Returns the decoded value of a Base64 string base64_authorization_header
        """
        if (
           not base64_authorization_header or
           not isinstance(base64_authorization_header, str)):
            return None
        try:
            return base64.b64decode(base64_authorization_header).decode('utf-8')
        except Exception as e:
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> (str, str):
        """
        Returns the user email and password from the Base64 decoded value.
        """
        if (
           not decoded_base64_authorization_header or
           not isinstance(decoded_base64_authorization_header, str) or
           ':' not in decoded_base64_authorization_header):
            return (None, None)
        return tuple(decoded_base64_authorization_header.split(':',1))

    def user_object_from_credentials(self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """
        Returns the User instance based on his email and password.
        """
        if (
           not user_email or
           not isinstance(user_email, str) or
           not user_pwd or
           not isinstance(user_pwd, str)
           ):
            return None
        objects = User().search({"email": user_email})
        if not objects:
            return None
        if objects[0].is_valid_password(user_pwd):
            return objects[0]
        else:
            return None
