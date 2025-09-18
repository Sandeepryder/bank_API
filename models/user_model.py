from pydantic import BaseModel
from datetime import datetime

class LoginUser(BaseModel):
    username: str
    password: str

class RegisterUser(BaseModel):
    username: str
    password: str
    balance: float
    transactions: list = []

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None


class Transaction(BaseModel):
    amount: float
    
