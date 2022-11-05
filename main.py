from fastapi import FastAPI
from scrap import ipCheck

app = FastAPI()

@app.get("/")
def root():
    return ipCheck()