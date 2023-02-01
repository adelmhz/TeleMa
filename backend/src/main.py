from fastapi import FastAPI

from core import models
from apps.account.views import router as account_router
from apps.services.views import router as service_router
from apps.user.views import router as user_router
from db.database import engin

app = FastAPI()
app.include_router(account_router)
app.include_router(service_router)
app.include_router(user_router)

@app.get('/')
def index():
    return {'message': 'Hello world!'}

models.Base.metadata.create_all(engin)