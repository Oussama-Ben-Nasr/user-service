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
    def __init__(self, db_url="sqlite:///example.db"):
        # initialize the db connection
        engine = create_engine(db_url, echo=True)
        self.db_connection = engine
        self.db_url = db_url
        Base.metadata.create_all(engine)
        super().__init__()
    
