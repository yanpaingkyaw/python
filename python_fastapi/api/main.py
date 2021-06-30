from fastapi import FastAPI
from pydantic import BasedModel
from typing import Optional

app = FastAPI()

@app.get("/")
def read_root():
    return {"greeeting": "Welcome from FastAPI" }
