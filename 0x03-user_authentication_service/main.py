#!/usr/bin/env python3
"""
Main file
"""
from requests import post, put

BASE_URL = 'http://localhost:5000'
SESSION_PATH = 'sessions'
USERS_PATH = 'users'
PROFILE_PATH = 'profile'
RESET_PATH = 'reset_password'
SEP = '/'


def register_user(email: str, password: str) -> None:
    """function to test with requests module the server"""
    resp = post(BASE_URL + SEP + USERS_PATH, data={'email': email,
                                                   'password': password})
    print(resp.json())


def log_in_wrong_password(email: str, password: str) -> None:
    """function to test with requests module the server"""
    resp = post(BASE_URL + SEP + SESSION_PATH, data={'email': email,
                                                     'password': password})
    print(resp.json())


def log_in(email: str, password: str) -> str:
    """function to test with requests module the server"""
    pass


def profile_unlogged() -> None:
    """function to test with requests module the server"""
    pass


def profile_logged(session_id: str) -> None:
    """function to test with requests module the server"""
    pass


def log_out(session_id: str) -> None:
    """function to test with requests module the server"""
    pass


def reset_password_token(email: str) -> str:
    """function to test with requests module the server"""
    pass


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """function to test with requests module the server"""
    pass


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"

if __name__ == "__main__":
    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    # profile_unlogged()
    # session_id = log_in(EMAIL, PASSWD)
    # profile_logged(session_id)
    # log_out(session_id)
    # reset_token = reset_password_token(EMAIL)
    # update_password(EMAIL, reset_token, NEW_PASSWD)
    # log_in(EMAIL, NEW_PASSWD)
