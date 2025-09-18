from fastapi import APIRouter, FastAPI
from .auth import router as auth_routers
from .transactions import router as bank_routers

routers = APIRouter() 


routers.include_router(auth_routers)
routers.include_router(bank_routers)
