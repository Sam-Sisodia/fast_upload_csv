from pydantic import BaseModel


class Item(BaseModel):
    name: str
    email: str
    phone :  str








class UserSchema(BaseModel):
    id : int
    email: str
    phone:str
    hashed_password: str