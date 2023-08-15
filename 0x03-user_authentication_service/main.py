#!/usr/bin/env python3
"""
Module to query the web browser.
"""
import requests


def register_user(email: str, password: str) -> None:
    """
    Registers a new user
    """
    test = requests.post('http://localhost:5000/users',
                      {'email': email, 'password': password})
    assert test.status_code == 200


def log_in_wrong_password(email: str, password: str) -> None:
    """
    Login instance with wrong password
    """
    test = requests.post('http://localhost:5000/sessions',
                      {'email': email, 'password': password})
    assert test.status_code == 401


def log_in(email: str, password: str) -> str:
    """
    login instance with correct password
    """
    test = requests.post('http://localhost:5000/sessions',
                      {'email': email, 'password': password})
    assert test.status_code == 200
    return test.cookies.get('session_id')


def profile_unlogged() -> None:
    """
    Unlogged profile
    """
    test = requests.get('http://localhost:5000/profile')
    assert test.status_code == 403


def profile_logged(session_id: str) -> None:
    """
    Logged profile
    """
    test = requests.get('http://localhost:5000/profile',
                     cookies={"session_id", session_id})
    assert test.status_code == 200


def log_out(session_id: str) -> None:
    """
    Log out instance
    """
    test = requests.delete('http://localhost:5000/sessions',
                        cookies={"session_id", session_id})
    assert test.status_code == 200


def reset_password_token(email: str) -> str:
    """
    Reset password token instance
    """
    test = requests.post('http://localhost:5000/reset_password',
                      {'email': email})
    assert test.status_code == 200


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """
    Update password instance
    """
    test = requests.put('http://locahost:5000/reset_password',
                     {'email': email, 'reset_token': reset_token,
                      'new_password': new_password})
    assert test.status_code == 200


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
