#!/usr/bin/env python3
"""
module to check auth
"""
from typing import List, TypeVar
from flask import request


class Auth:
    """class to represent authentication"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """method for check require auth

        Args:
            path (str): _description_
            excluded_paths (List[str]): _description_

        Returns:
            bool: returns False
            path and excluded_paths will be used later,
            now, you don’t need to take care of them
        """
        if path is None or\
            excluded_paths is None or\
                len(excluded_paths) == 0:
            return True
        if path[-1] != '/':
            path = path + '/'
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """method to add header

        Args:
            request (_type_, optional): flask req obj

        Returns:
            str: None - request will be the Flask request object
        """
        print(request.path)
        print(request)
        print(request.authorization)
        if request is None\
            or request.authorization is None:
            return None
        else:
            return request.authorization

    def current_user(self, request=None) -> TypeVar('User'):
        """current user
        returns:
            returns None - request will be the Flask request object
        """
        return None
