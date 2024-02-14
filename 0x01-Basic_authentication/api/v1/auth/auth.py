#!/usr/bin/env python3
"""
module to check auth
""" 
from typing import TypeVar
from flask import request


class Auth:
    """class to represent authentication"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """method for check require auth

        Args:
            path (str): _description_
            excluded_paths (List[str]): _description_

        Returns:
            bool: returns False - 
            path and excluded_paths will be used later,
            now, you don’t need to take care of them
        """
        pass


    def authorization_header(self, request=None) -> str:
        """method to add header

        Args:
            request (_type_, optional): flask req obj

        Returns:
            str: None - request will be the Flask request object
        """
        pass
    
    def current_user(self, request=None) -> TypeVar('User'):
        """current user
        returns:
            returns None - request will be the Flask request object
        """
