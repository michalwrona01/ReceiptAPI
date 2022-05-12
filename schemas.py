from datetime import date, datetime
from typing import Optional, List
from pydantic import BaseModel
from fastapi import Body


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True


class ReceiptBase(BaseModel):
    shop_name: str
    address: str
    date_add_receipt: Optional[date] = Body(None)
    date_shop_products: Optional[datetime] = Body(None)
    number_receipt: int
    NIP_number_shop: int


class ReceiptCreate(ReceiptBase):
    owner_id: int


class ProductBase(BaseModel):
    name: str
    price: int
    amount: int


class ProductCreate(ProductBase):
    receipt_id: int


class Product(ProductCreate):
    id: int


class Receipt(ReceiptBase):
    id: int
    owner_id: int
    products: List[Product] = []

    class Config:
        orm_mode = True
