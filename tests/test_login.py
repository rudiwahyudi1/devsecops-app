# tests/test_login.py

from backend.app import login

def test_login_success():
    assert login("admin", "admin") is True

def test_login_fail():
    assert login("user", "wrong") is False
