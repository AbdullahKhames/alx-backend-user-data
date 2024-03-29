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
        for current_path in excluded_paths:
            if path[-1] == '/':
                path = path.split("/")[-2]
            else:
                path = path.split("/")[-1]
            current_path = current_path.split("/")[-1]
            if current_path.endswith('*') and current_path[0:-1] in path:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """method to add header

        Args:
            request (_type_, optional): flask req obj

        Returns:
            str: None - request will be the Flask request object
        """
        if request is None\
           or request.headers.get('Authorization', None) is None:
            return None
        else:
            return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """current user
        returns:
            returns None - request will be the Flask request object
        """
        return None
