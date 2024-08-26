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
    
    def __repr__(self) -> str:
        return "User(id={self.user_id!r}, name={self.user_name!r})"

Base.metadata.create_all(engine)
app = FastAPI()

@app.post("/register")
def register(user_name: str, password: str):
    user = User(
        user_id = str(uuid.uuid4()),
        email = "",
        user_name = user_name,
        password  = password,
        age=-1
    )

    with Session(engine) as session:
        # make sure username does not exist
        stmt = select(User).where(User.user_name == user_name)
        for u in session.scalars(stmt):
            print(u)
            return {"User exist please choose another username"}

        # add user
        session.add(user)
        session.commit()

    return {"user_name": user_name}


@app.post("/login")
def register(user_name: str, password: str):
    with Session(engine) as session:
        stmt = select(User).where(User.user_name == user_name)
        for u in session.scalars(stmt):
            if(u.password != password):
                return {"Wrong password!"}
            return {"user_name": u.user_name}
        return {"User not found!"}

