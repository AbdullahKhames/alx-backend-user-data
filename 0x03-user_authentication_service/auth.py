#!/usr/bin/env python3
"""module for implementing auth module functionalities"""
from bcrypt import gensalt, hashpw
from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """method that takes in a password and returns its hash"""
    return hashpw(password.encode('utf-8'), gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """method to regiseter user"""
        existing_user = self._db.find_user_by(email=email)
        if existing_user:
            raise ValueError
        hashed_pw = _hash_password(password)
        user = self._db.add_user(email, hashed_pw)
        return user
