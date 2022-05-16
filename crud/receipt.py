from sqlalchemy.orm import Session
from db import models
from schemas.receipt import ReceiptCreate


def get_receipts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Receipt).offset(skip).limit(limit).all()


def get_receipt_by_id(db: Session, receipt_id: int):
    return db.query(models.Receipt).filter(models.Receipt.id == receipt_id).first()


def post_receipt(db: Session, receipt: ReceiptCreate):
    db_receipt = models.Receipt(shop_name=receipt.shop_name,
                                address=receipt.address,
                                date_add_receipt=receipt.date_add_receipt,
                                date_shop_products=receipt.date_shop_products,
                                number_receipt=receipt.number_receipt,
                                NIP_number_shop=receipt.NIP_number_shop,
                                owner_id=receipt.owner_id)
    db.add(db_receipt)
    db.commit()
    db.refresh(db_receipt)
    return db_receipt
  
  
def post_receipt_by_image(db: Session, receipts_data):
    pass

