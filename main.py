from fastapi import FastAPI, Request
from db import models
from db.database import engine

models.Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.get("/")
def home(request: Request):
    return {"message": "Hello!",
            "documentation": request.url._url + "docs"}


from endpoints.user import *
from endpoints.product import *
from endpoints.receipt import *
