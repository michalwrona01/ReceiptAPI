from sqlalchemy import Boolean, Column, Integer, String, Date, DateTime, Float, ForeignKey
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
    __tablename__ = "receipt"

    id = Column(Integer, primary_key=True, index=True)
    shop_name = Column(String)
    address = Column(String)
    date_add_receipt = Column(Date, default=func.now())
    date_shop_products = Column(DateTime(timezone=True), default=func.now())
    number_receipt = Column(Integer)
    NIP_number_shop = Column(Integer)
    products = relationship("Product")
    owner_id = Column(Integer, ForeignKey("users.id"))


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Float)
    amount = Column(Float)

    receipt_id = Column(Integer, ForeignKey("receipt.id"))
