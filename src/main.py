from fastapi import FastAPI

from core import models
from account.views import router as account_router
from db.database import engin

app = FastAPI()
app.include_router(account_router)

@app.get('/')
def index():
    return {'message': 'Hello world!'}

models.Base.metadata.create_all(engin)