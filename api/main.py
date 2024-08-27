from sqlalchemy import select
from sqlalchemy.orm import Session
from ..user.models import UserLoginRequest, UserRegisterRequest, FailedRequest, UserRegisterResponse
from ..user import UserService, User

app = UserService()

@app.post("/register")
def register(request: UserRegisterRequest):
    # TODO: add validation on user input
    user = User(
        email = request.email,
        user_name = request.user_name,
        password  = request.password,
    )

    with Session(app.db_connection) as session:
        # make sure username does not exist
        stmt = select(User).where(User.user_name == request.user_name)
        for user in session.scalars(stmt):
            return {"message": "User exist please choose another username"}

        # add user
        session.add(user)
        session.commit()

    return {"user_name": request.user_name}


@app.post("/login", response_model=UserRegisterResponse | FailedRequest)
def register(request: UserLoginRequest):
    with Session(app.db_connection) as session:
        stmt = select(User).where(User.user_name == request.user_name)
        for matching_user in session.scalars(stmt):
            if (matching_user.password != request.password):
                return {"message": "Wrong password!"}
            return {"user_name": matching_user.user_name}
        return {"message": "User not found!"}

