from mangum import Mangum
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello Harsh"}

@app.get("/items")
async def root():
    return {"item": "Mango"}

handler = Mangum(app=app)


