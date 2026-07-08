from pydantic import BaseModel
from pydantic import EmailStr


class UserCreate(BaseModel):

    firstname: str

    lastname: str

    email: EmailStr

    password: str

    profession: str

    monthly_income: int


class UserResponse(BaseModel):

    id: int

    firstname: str

    lastname: str

    email: EmailStr

    profession: str

    monthly_income: int

    class Config:
        from_attributes = True