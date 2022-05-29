from fastapi import Depends, HTTPException, UploadFile, File
from schemas.receipt import Receipt, ReceiptCreate
from sqlalchemy.orm import Session
from db.database import get_db
from crud.receipt import get_receipts, get_receipt_by_id, post_receipt
from crud.user import get_user_by_id
from main import app
import requests
import json


@app.get("/receipts/", response_model=list[Receipt])
def read_receipts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    receipts = get_receipts(db, skip=skip, limit=limit)
    return receipts


@app.post("/receipts/", response_model=Receipt)
def create_receipt(receipt: ReceiptCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_id(db=db, user_id=receipt.owner_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return post_receipt(db=db, receipt=receipt)


@app.post("/receipts-image/")
def create_receipt(file: UploadFile = File(...)):
    if file is None:
        raise HTTPException(status_code=404, detail="Image is empty")

    payload = {'isOverlayRequired': False,
               'apikey': "K88243565988957",
               'language': "pol",
               "OCREngine": 2,
               'scale': True,
               'isTable': True,
               'detectOrientation': True,
               }

    r = requests.post('https://api.ocr.space/parse/image',
                      files={file.filename: file.file},
                      data=payload,
                      )

    content = r.content
    parsed_text = json.loads(content)['ParsedResults'][0]['ParsedText']

    return {"parsed_text": parsed_text}


@app.get("/receipts/{receipt_id}", response_model=Receipt)
def read_receipt(receipt_id: int, db: Session = Depends(get_db)):
    db_receipt = get_receipt_by_id(db, receipt_id=receipt_id)
    if db_receipt is None:
        raise HTTPException(status_code=404, detail="Receipt not found")
    return db_receipt
