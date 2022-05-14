from datetime import date, datetime
from typing import Optional, List
from pydantic import BaseModel
from fastapi import Body
from .product import Product


class ReceiptBase(BaseModel):
    shop_name: str
    address: str
    date_add_receipt: Optional[date] = Body(None)
    date_shop_products: Optional[datetime] = Body(None)
    number_receipt: int
    NIP_number_shop: int


class ReceiptCreate(ReceiptBase):
    owner_id: int


class Receipt(ReceiptBase):
    id: int
    owner_id: int
    products: List[Product] = []

    class Config:
        orm_mode = True
