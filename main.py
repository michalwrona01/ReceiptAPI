from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.get("/receipts/", response_model=list[schemas.Receipt])
def read_receipts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    receipts = crud.get_receipts(db, skip=skip, limit=limit)
    return receipts


@app.post("/receipts/", response_model=schemas.Receipt)
def create_receipt(receipt: schemas.ReceiptCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user(db=db, user_id=receipt.owner_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return crud.create_receipt(db=db, receipt=receipt)


@app.get("/receipts/{receipt_id}", response_model=schemas.Receipt)
def read_receipt(receipt_id: int, db: Session = Depends(get_db)):
    db_receipt = crud.get_receipt_by_id(db, receipt_id=receipt_id)
    if db_receipt is None:
        raise HTTPException(status_code=404, detail="Receipt not found")
    return db_receipt


@app.post("/products/", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db=db, product=product)


@app.get("/products/{receipt_id}", response_model=list[schemas.Product])
def read_product(receipt_id: int, db: Session = Depends(get_db)):
    db_product = crud.get_products_by_receipt_id(db=db, receipt_id=receipt_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product
