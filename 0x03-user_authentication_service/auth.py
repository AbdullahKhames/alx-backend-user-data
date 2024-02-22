#!/usr/bin/env python3
"""module for implementing auth module functionalities"""
from bcrypt import gensalt, hashpw


def _hash_password(password: str) -> bytes:
    """method that takes in a password and returns its hash"""
    return hashpw(password.encode('utf-8'), gensalt())
