from app import jwt


def test_create_access_token():
    data = {"sub": "user1"}
    token = jwt.create_access_token(data)
    assert isinstance(token, str) and token


def test_token_contains_sub():
    data = {"sub": "user2"}
    token = jwt.create_access_token(data)
    payload = jwt.jwt.decode(token, jwt.SECRET_KEY, algorithms=[jwt.ALGORITHM])
    assert payload.get("sub") == "user2"
