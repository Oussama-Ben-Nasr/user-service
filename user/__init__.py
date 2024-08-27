from fastapi import FastAPI
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import create_engine
from sqlalchemy.orm import Mapped
from sqlalchemy import String

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user_acount"
    email: Mapped[str] = mapped_column(String(30), primary_key=True)
    user_name: Mapped[str] = mapped_column(String(30))
    password: Mapped[str] = mapped_column(String)


class UserService(FastAPI):
    def __init__(self):
        # initialize the db connection
        engine = create_engine("sqlite:///example.db", echo=True)
        self.db = engine
        Base.metadata.create_all(engine)
        super().__init__()
    
