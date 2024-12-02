from fastapi import APIRouter, FastAPI, Response, status
import redis
import os
from app.schemas import EventItem, EventUpdate
from app.event import Event
from app.sender import Sender


REDIS_HOST = os.getenv('REDIS_HOST')
REDIS_PORT = os.getenv('REDIS_PORT')

router = APIRouter()
sender = Sender()
redis_db = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

@router.post("/events")
async def create_event(event_item: EventItem, response: Response):
    event = Event()
    event.build_event(event_item.user_id, event_item.description)
    sender.send(event)
    response.status_code = status.HTTP_201_CREATED

@router.get("/events/{event_id}")
async def return_event(event_id: str):
    event = redis_db.hgetall(f'event_id:{event_id}')
    return event

@router.patch("/events/{event_id}")
async def update_status(event_id: str, event_update: EventUpdate, response: Response):
    redis_db.hset(f'event_id:{event_id}', 'status', status)
    response.status_code = status.HTTP_200_OK

