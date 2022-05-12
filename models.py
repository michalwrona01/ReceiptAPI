from sqlalchemy import Boolean, Column, Integer, String, Float, ForeignKey, Date, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    receipts = relationship("Receipt")


class Receipt(Base):
    __tablename__ = "receipts"

    id = Column(Integer, primary_key=True, index=True)
    shop_name = Column(String)
    address = Column(String)
    date_add_receipt = Column(Date, default=func.now())
    date_shop_products = Column(DateTime, default=func.now())
    number_receipt = Column(Integer)
    NIP_number_shop = Column(Integer)
    owner_id = Column(Integer, ForeignKey("users.id"))

    products = relationship("Product")


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Float)
    amount = Column(Float)

    receipt_id = Column(Integer, ForeignKey("receipts.id"))
