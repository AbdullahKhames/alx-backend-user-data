#!/usr/bin/env python3
"""module to implement basic auth"""

from api.v1.auth.auth import Auth


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
        pass
