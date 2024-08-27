from fastapi.testclient import TestClient
from api.main import app
from user.models import UserRegisterRequest, UserRegisterResponse, FailedRequest, UserLoginResponse, UserLoginRequest

client = TestClient(app)

fake_db = {
    "jane_doe": {"user_name": "jane_doe", "email": "jane_doe@email.com", "password": "1234"},
}


@app.post("/register/", response_model=UserRegisterResponse | FailedRequest)
async def register_user(register_request: UserRegisterRequest):
    if register_request.user_name in fake_db.keys():
        return {"message": "User exist please choose another username"}
    fake_db[register_request.user_name] = register_request
    return {"user_name": "john_doe"}


@app.post("/login/", response_model=UserLoginResponse | FailedRequest)
async def register_user(login_request: UserLoginRequest):
    if not login_request.user_name in fake_db.keys():
        return {"message": "User not found!"}
    if login_request.password != fake_db[login_request.user_name].password:
        return {"message": "Wrong password!"}
    return {"user_name": login_request.user_name}

def test_register_user():
    response = client.post(
        "/register/",
        json={"user_name": "john_doe",
              "email": "john_doe@email.com",
              "password": "12345!"},
    )
    assert response.status_code == 200
    assert response.json() == {"user_name": "john_doe"}


def test_register_existing_user():
    response = client.post(
        "/register/",
        json={"user_name": "john_doe",
              "email": "john_doe@email.com",
              "password": "12345!"},
    )
    assert response.status_code == 200
    assert response.json() == {"message": "User exist please choose another username"}


def test_login_registered_user():
    response = client.post(
        "/login/",
        json={"user_name": "john_doe",
              "password": "12345!"},
    )
    assert response.status_code == 200
    assert response.json() == {"user_name": "john_doe"}
