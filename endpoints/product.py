from schemas.product import Product, ProductCreate
from fastapi import Depends, HTTPException
from db.database import get_db
from sqlalchemy.orm import Session
from main import app
from crud.product import post_product, get_products_by_receipt_id


@app.post("/products/", response_model=Product)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    return post_product(db=db, product=product)


@app.get("/products/{receipt_id}", response_model=list[Product])
def read_product(receipt_id: int, db: Session = Depends(get_db)):
    db_product = get_products_by_receipt_id(db=db, receipt_id=receipt_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product
