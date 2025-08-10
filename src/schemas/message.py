from pydantic import BaseModel
from typing import Optional
import bson, datetime

class ModerationResult(BaseModel):
    toxicity: Optional[float] = None
    identity_attack: Optional[float] = None
    insult: Optional[float] = None
    obscene: Optional[float] = None
    
class Message(BaseModel):
    id: bson.ObjectId = bson.ObjectId()
    created_at: datetime.datetime = datetime.datetime.now()
    user_id: bson.ObjectId
    text: str
    moderation_result: ModerationResult
    