import pytest
from datetime import timedelta
from app import jwt

def test_create_access_token_returns_token():
    data = {"sub": "user1"}
    token = jwt.create_access_token(data)
    assert isinstance(token, str)
    assert token != ""

def test_create_access_token_expiry():
    data = {"sub": "user2"}
    expires = timedelta(minutes=1)
    token = jwt.create_access_token(data, expires_delta=expires)
    payload = jwt.jwt.decode(token, jwt.SECRET_KEY, algorithms=[jwt.ALGORITHM])
    assert "exp" in payload

def test_verify_token_valid():
    data = {"sub": "user3"}
    token = jwt.create_access_token(data)
    payload = jwt.jwt.decode(token, jwt.SECRET_KEY, algorithms=[jwt.ALGORITHM])
    assert payload["sub"] == "user3"