from sqlmodel import Field, SQLModel

from datetime import datetime


class Dog(SQLModel):
    __tablename__ = "Dogs"
    name:str | None = Field(default = None,min_length=1,max_length=100)
    size: str | None = Field(default = None,min_length=1,max_length=100)
    dangerous : bool = Field(default = False)
    sterilized : bool = Field(default = False)
    breed : bool = Field(default = False)




class Dogsid(Dog, table = True):
    __tablename__ = "DogsIds"
    id : int|None = Field(default = None,primary_key=True)

class uptadedog(Dog):
    name: str | None = Field(default=None, min_length=1, max_length=100)
    size: str | None = Field(default=None, min_length=1, max_length=100)
    dangerous: bool = Field(default=False)
    sterilized: bool = Field(default=False)
    breed: bool = Field(default=False)



