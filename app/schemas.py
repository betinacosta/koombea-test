from pydantic import BaseModel


class EventItem(BaseModel):
    user_id: str
    description: str

class EventUpdate(BaseModel):
    status: str
