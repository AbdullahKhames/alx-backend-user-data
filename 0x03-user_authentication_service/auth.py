#!/usr/bin/env python3
"""module for implementing auth module functionalities"""
from typing import Union

from bcrypt import gensalt, hashpw, checkpw
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4


def _hash_password(password: str) -> bytes:
    """method that takes in a password and returns its hash"""
    return hashpw(password.encode('utf-8'), gensalt())


def _generate_uuid() -> str:
    """generates uuid"""
    return str(uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """method to regiseter user"""
        try:
            existing_user = self._db.find_user_by(email=email)
            if existing_user:
                raise ValueError(f'User {email} already exists')
        except NoResultFound as ex:
            pass
        hashed_pw = _hash_password(password)
        user = self._db.add_user(email, hashed_pw)
        return user

    def valid_login(self, email: str, password: str) -> bool:
        """to check for email and password"""
        if not email or not password:
            return False
        try:
            user = self._db.find_user_by(email=email)
            user_bytes = password.encode('utf-8')
            return checkpw(user_bytes, user.hashed_password)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> Union[str, None]:
        """creates a session for the user"""
        try:
            user = self._db.find_user_by(email=email)
            user.session_id = _generate_uuid()
            self._db.update_user(user.id)
            return user.session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, sess_id: str) -> Union[User, None]:
        """returns user for a given session id"""
        try:
            return self._db.find_user_by(session_id=sess_id)
        except NoResultFound:
            return None

    def destroy_session(self, email: str) -> None:
        """creates a session for the user"""
        try:
            user = self._db.find_user_by(email=email)
            user.session_id = None
            self._db.update_user(user.id)
            return None
        except NoResultFound:
            return None
