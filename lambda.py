from mangum import Mangum
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello Harsh Vardhan"}
<<<<<<< HEAD
=======

>>>>>>> f7d19e1d9a88667e9784cf0889a9da11d99bca6a
handler = Mangum(app=app)