#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine, and_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from sqlalchemy.exc import InvalidRequestError
from user import Base, User
from sqlalchemy.orm.exc import NoResultFound


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ adds user to database
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """ find user function """
        my_filters = set()
        for k, v in kwargs.items():
            if hasattr(User, k):
                my_filters.add(getattr(User, k) == v)
            else:
                raise InvalidRequestError
        user = self._session.query(User).filter(and_(*my_filters)).first()
        if user is None:
            raise NoResultFound
        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """method that updates the user entity in db"""
        user = self.find_user_by(id=user_id)
        for k, v in kwargs.items():
            if not hasattr(User, k):
                raise ValueError
            setattr(user, k, v)
        self._session.commit()