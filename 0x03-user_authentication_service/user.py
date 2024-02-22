#!/usr/bin/env python3
"""module for implementing user module functionalities"""


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250))
    reset_token = Column(String(250))

    def __init__(self, *args, **kwargs):
        """method to construct object"""
        for k, v in kwargs.items():
            if hasattr(self, k):
                setattr(self, k, v)
