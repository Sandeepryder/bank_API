import datetime
from fastapi import APIRouter, Depends, HTTPException

from controllers.jwt import get_current_user
from helpers.handlers import load_db, save_db
from models.user_model import Transaction

router = APIRouter(prefix="/transactions", tags=["transactions"])


@router.post("/deposit")
def deposit(transaction :Transaction , current_user: str = Depends(get_current_user)):
    try :
       
        db = load_db()
        username = current_user["sub"]

        result = next((u for u in db["users"] if u["username"] == username), None)
        if not result :
            raise HTTPException(status_code=404, detail="User not found")
       
        result["balance"] += transaction.amount

        result["transactions"].append({
            "type": "deposit",
            "amount": transaction.amount
        })

        save_db(db)
        return {"msg": "Deposit successful", "balance": result["balance"]}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error") from e
    


@router.post("/withdraw")
def withdraw(transaction : Transaction, current_user: str = Depends(get_current_user)):
    try :
        db = load_db()
        username = current_user["sub"]

        result = next((u for u in db["users"] if u["username"] == username), None)
        if not result:
            raise HTTPException(status_code=404, detail="User not found")

        if transaction.amount > result["balance"]:
            raise HTTPException(status_code=400, detail="Insufficient balance")

        result["balance"] -= transaction.amount

        result["transactions"].append({
            "type": "withdraw",
            "amount": transaction.amount
        })

        save_db(db)
        return {"msg": "Withdraw successful", "balance": result["balance"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error") from e
    


@router.get("/balance")
def balance(username: str , current_user: str = Depends(get_current_user)):
    try :
        db = load_db()
        user = next((u for u in db["users"] if u["username"] == username), None)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        return {"balance": user["balance"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error") from e
    
    

@router.get("/history")
def history(username: str , current_user: str = Depends(get_current_user)):
    try :
        db = load_db()
        user = next((u for u in db["users"] if u["username"] == username), None)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        return {"transactions": user["transactions"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error") from e
