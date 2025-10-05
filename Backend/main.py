from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def ruchka():
    return {"message": "Hello, World!"}