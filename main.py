# This is my email address: eazyisreal192@gmail.com
from fastapi import FastAPI
from routers import getfullname

app = FastAPI()

app.include_router(getfullname.router)
