#Mahesh SN
#added by Mahesh

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Inventory Management Service Running"}