#!/usr/bin/env python3
"""
Basic Auth Module inherits from Auth
"""

from api.v1.auth.auth import Auth
import base64


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
