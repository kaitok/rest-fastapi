from api.database import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship, backref
from .mixins import TimestampMixin


class Profile(Base, TimestampMixin):
    __tablename__ = "profile"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(length=100), nullable=False)
    last_name = Column(String(length=100), nullable=False)
