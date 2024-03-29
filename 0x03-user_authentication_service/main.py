#!/usr/bin/env python3
"""
Main file
"""
from requests import post, put, get, Session, delete

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
    assert resp.status_code == 200
    assert resp.json() == {"email": email,
                           "message": "user created"}


def log_in_wrong_password(email: str, password: str) -> None:
    """function to test with requests module the server"""
    resp = post(BASE_URL + SEP + SESSION_PATH, data={'email': email,
                                                     'password': password})
    assert resp.status_code == 401


def log_in(email: str, password: str) -> str:
    """function to test with requests module the server"""
    resp = post(BASE_URL + SEP + SESSION_PATH, data={'email': email,
                                                     'password': password})
    assert resp.status_code == 200
    assert resp.json() == {"email": email,
                           "message": "logged in"}
    cookie = resp.cookies.get('session_id')
    return cookie


def profile_unlogged() -> None:
    """function to test with requests module the server"""
    resp = get(BASE_URL + SEP + PROFILE_PATH)
    assert resp.status_code == 403


def profile_logged(session_id: str) -> None:
    """function to test with requests module the server"""
    with Session() as session:
        resp = session.get(BASE_URL + SEP + PROFILE_PATH,
                           cookies={'session_id': session_id})
        assert resp.status_code == 200
        assert resp.json() == {"email": EMAIL}


def log_out(session_id: str) -> None:
    """function to test with requests module the server"""
    with Session() as session:
        resp = session.delete(BASE_URL + SEP + SESSION_PATH,
                              cookies={'session_id': session_id})
        assert resp.status_code == 200
        assert resp.json() == {"message": "Bienvenue"}


def reset_password_token(email: str) -> str:
    """function to test with requests module the server"""
    resp = post(BASE_URL + SEP + RESET_PATH, data={'email': email})
    assert resp.status_code == 200
    token = resp.json().get('reset_token')
    assert resp.json() == {"email": email,
                           "reset_token": token}
    return token


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """function to test with requests module the server"""
    resp = put(BASE_URL + SEP + RESET_PATH,
               data={'email': email,
                     'reset_token': reset_token,
                     'new_password': new_password})
    assert resp.status_code == 200
    assert resp.json() == {"email": email,
                           "message": "Password updated"}


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"

if __name__ == "__main__":
    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
