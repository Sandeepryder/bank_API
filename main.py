from fastapi import FastAPI
from controllers import routers as api_routers

app = FastAPI(title="Banks API", version="1.0.0")

@app.get("/start")
def read_root():
    return {"message": "Welcome to the Banks API"}


app.include_router(api_routers)