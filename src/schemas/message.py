from pydantic import BaseModel
import bson, datetime

# id, user_id, text, created_at, moderation_result
class Message(BaseModel):
    id: bson.ObjectId = bson.ObjectId()
    created_at: datetime.datetime = datetime.datetime.now()
    user_id: bson.ObjectId
    text: str
    moderation_result: str = "pending"  # default to pending
    