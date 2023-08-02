#!/usr/bin/env python3
"""
Hashing with bcrypt package
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Returns salted, hash password.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
