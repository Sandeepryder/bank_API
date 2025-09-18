from fastapi import APIRouter, FastAPI, HTTPException
from fastapi import Depends

from helpers.handlers import load_db, save_db
from models.user_model import LoginUser, RegisterUser
from .jwt import create_access_token, get_current_user
from helpers.security import get_password_hash, verify_password

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register")
def register(req : RegisterUser ):
    try :
        db = load_db()
        if any(u["username"] == req.username for u in db["users"]):
            raise HTTPException(status_code=400, detail="User already exists")
        
        db["users"].append({
            "username": req.username,
            "password": get_password_hash(req.password),
            "balance": req.balance,
            "transactions": []
        })
        save_db(db)
        return {"msg": "User created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error") from e


@router.post("/login")
def login(req :LoginUser):
    try :
        db = load_db()
        user = next((u for u in db["users"] if u["username"] == req.username), None)
        if not user or not verify_password(req.password, user["password"]):
            
            raise HTTPException(status_code=400, detail="Invalid credentials")
        # Generate JWT token (mocked here)
        token =create_access_token(data={"sub": user["username"]})
        return {"token": token}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error") from e
