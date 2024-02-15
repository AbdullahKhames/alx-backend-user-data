#!/usr/bin/env python3
"""module to implement basic auth"""

import base64
from typing import TypeVar
from api.v1.auth.auth import Auth
from models.base import DATA, Base
from models.user import User


class BasicAuth(Auth):
    """class that implements basic authentication"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """extracts base64 auth header

        Args:
            authorization_header (str): the authorization header

        Returns:
            str: _description_
        """
        if authorization_header is None or\
            type(authorization_header) is not str or\
                not authorization_header.startswith('Basic '):
            return None
        else:
            return authorization_header.split(' ')[1]

    def decode_base64_authorization_header(
                                            self,
                                            base64_authorization_header:
                                            str) -> str:
        """method to decode

        Args:
            base64_authorization_header (str): base 64 header

        Returns:
            str: the decoded
        """
        data = None
        if base64_authorization_header is None or\
           type(base64_authorization_header) is not str:
            return data
        try:
            data = base64.b64decode(base64_authorization_header)
            data = data.decode('UTF-8')
        except Exception as ex:
            return data
        else:
            return data

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                 str) -> (str, str):
        """function to extract credentials

        Args:
            self (_type_): _description_
            decoded_base64_authorization_header (_type_):
            decoded header
        """
        if decoded_base64_authorization_header is None or\
            type(decoded_base64_authorization_header) is not str or\
                not decoded_base64_authorization_header.__contains__(':'):
            return (None, None)
        else:
            return (decoded_base64_authorization_header.split(':'))

    def user_object_from_credentials(self,
                                     user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """user obj from cred

        Args:
            self (_type_): _description_
            user_email (str): email extracted
            user_pwd (str): pw extracted
        """
        if user_email is None or\
            type(user_email) is not str or\
                user_pwd is None or\
                    type(user_pwd) is not str:
            return None
        Base.load_from_file()
        found = False
        if DATA['User'] is None or\
            len(DATA['User']) == 0:
                return None
        user = None
        for val in DATA['User'].values():
            if val.email == user_email:
                user = User(**{
                    'email': user_email,
                    '_password': val.password,
                    'first_name': val.first_name,
                    'last_name': val.last_name
                })
                if user.is_valid_password(user_pwd):
                    found = True
        if not found:
            return None
        else:
            return user
