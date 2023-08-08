#!/usr/bin/env python3
"""
UserSession module
"""

from models.base import Base


class UserSession(Base):
    """
    Inherits from Base
    """

    def __init__(self, *args: list, **kwargs: dict):
        """
        Initializes User instance
        """
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
