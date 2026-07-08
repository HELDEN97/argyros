from pydantic import BaseModel, EmailStr


class RegisterRequest(BaseModel):
    firstname: str
    lastname: str
    email: EmailStr
    password: str
    profession: str = "student"
    monthly_income: int = 0


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"