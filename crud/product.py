from sqlalchemy.orm import Session
from db import models
from schemas.product import ProductCreate


def create_product(db: Session, product: ProductCreate):
    db_product = models.Product(name=product.name, price=product.price,
                                amount=product.amount, receipt_id=product.receipt_id)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def get_products_by_receipt_id(db: Session, receipt_id: int):
    return db.query(models.Product).filter(models.Product.receipt_id == receipt_id).all()
