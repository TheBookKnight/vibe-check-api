from pydantic import BaseModel
import bson, datetime

class User(BaseModel):
    id: bson.ObjectId = bson.ObjectId()
    created_at: datetime.datetime = datetime.datetime.now()
    username: str
    email: str 
