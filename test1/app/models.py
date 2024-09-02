from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


from pydantic import BaseModel


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    phone  = Column(String)
    address = Column(String)
    hashed_password = Column(String)
    pin = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)

    # items = relationship("Item", back_populates="owner")



# class Item(Base):
#     __tablename__ = "Itme"

#     id = Column(Integer, primary_key=True)
#     name  = Column(String)
    