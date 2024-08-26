from fastapi import FastAPI
import uuid
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import create_engine
from sqlalchemy.orm import Mapped
from sqlalchemy import String
from typing import Optional
from sqlalchemy import select
from sqlalchemy.orm import Session
from pydantic import BaseModel

class Base(DeclarativeBase):
    pass

engine = create_engine("sqlite:///example.db", echo=True) # TODO: refactor to better naming!

class User(Base):
    __tablename__ = "user_acount"
    user_id: Mapped[str] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(30))
    user_name: Mapped[str] = mapped_column(String(30))
    password: Mapped[str] = mapped_column(String)
    age: Mapped[Optional[int]]

class UserCreds(BaseModel):
    user_name: str
    password: str

Base.metadata.create_all(engine)
app = FastAPI()

@app.post("/register")
def register(creds: UserCreds):
    user = User(
        user_id = str(uuid.uuid4()),
        email = "",
        user_name = creds.user_name,
        password  = creds.password,
        age=-1
    )

    with Session(engine) as session:
        # make sure username does not exist
        stmt = select(User).where(User.user_name == creds.user_name)
        for user in session.scalars(stmt):
            return {"User exist please choose another username"}

        # add user
        session.add(user)
        session.commit()

    return {"user_name": creds.user_name}

@app.post("/login")
def register(creds: UserCreds):
    with Session(engine) as session:
        stmt = select(User).where(User.user_name == creds.user_name)
        for matching_user in session.scalars(stmt):
            if (matching_user.password != creds.password):
                return {"Wrong password!"}
            return {"user_name": matching_user.user_name}
        return {"User not found!"}

