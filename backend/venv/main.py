from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
app = FastAPI()

@app.get('/')
def root_path():
    return ("main page")