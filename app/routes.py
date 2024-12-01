from fastapi import APIRouter
from app.schemas import EventItem
from app.event import Event
from app.sender import Sender
from app.consumer import Consumer

router = APIRouter()
consumer = Consumer()
consumer.start_listening()

@router.post("/events")
async def create_event(event_item: EventItem):
    event = Event()
    event.build_event(event_item.user_id, event_item.description)

    sender = Sender()
    sender.send(event)

@router.get("/events/{event_id}")
async def return_event(event_id: str):
    return event_id

