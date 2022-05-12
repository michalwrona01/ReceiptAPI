from sqlalchemy.orm import Session
import models
import schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_receipt_by_id(db: Session, receipt_id: int):
    return db.query(models.Receipt).filter(models.Receipt.id == receipt_id).first()


def create_receipt(db: Session, receipt: schemas.ReceiptCreate):
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
