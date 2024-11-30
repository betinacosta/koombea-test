from fastapi import APIRouter
from app.schemas import EventItem

router = APIRouter()

@router.post("/events")
async def create_event(event_item: EventItem):
    return {"event item": "Hello World"}

@router.get("/events/{event_id}")
async def return_event(event_id: str):
    return event_id

