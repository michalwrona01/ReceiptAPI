
# [ReceiptAPI](https://receipt-api-public.azurewebsites.net)

REST API for extracting data from pragueons and writing to the database


## Tech Stack

[Python 3.9](https://www.python.org/downloads/release/python-390/)

[FastAPI](https://fastapi.tiangolo.com/)

[PostgreSQL](https://www.postgresql.org.pl/)

[OCR Aspire](http://asprise.com/)


## Documentation

[Documentation](https://receipt-api-public.azurewebsites.net/docs)


## SQL Diagram
![receiptapi_diagram](https://user-images.githubusercontent.com/73277848/172056272-b681c345-ec15-4b4f-a54c-6b4caffff541.png)

## Installation

```bash
$ python3.9 -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt
$ uvicorn main:app --reload
```
    
