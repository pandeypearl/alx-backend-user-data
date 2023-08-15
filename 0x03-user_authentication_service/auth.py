#!/usr/bin/env python3
"""
Hashed Password
"""

import bcrypt


def _hash_password(password: str) -> str:
    """
    Takes in a password string arguments and returns bytes
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
