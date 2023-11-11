from pydantic import BaseModel, EmailStr, constr



class UserLogin(BaseModel):
    email: EmailStr
    password: str
