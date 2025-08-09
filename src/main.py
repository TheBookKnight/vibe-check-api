from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()
client = MongoClient("mongodb://localhost:27017")

@app.get("/")
def root():
    return {"message": "Hi! I'm the Vibe Check API!"}

@app.get("/health")
def get_db():
    try:
        # This will throw if the server is unreachable
        info = client.server_info()
        return {"message": "MongoDB connection successful!", "info": info}
    except Exception as e:
        return {"error": str(e)}
