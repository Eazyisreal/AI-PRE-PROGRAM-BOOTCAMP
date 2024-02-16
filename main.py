# This is my email address: eazyisreal192@gmail.com
from fastapi import FastAPI
from routers import getpdf

app = FastAPI()

app.include_router(getpdf.router)
