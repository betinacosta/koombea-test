import pytest

from app.event import Event


@pytest.fixture
def event():
    event = Event()
    yield event

def test_should_build_event_with_event_id(event):
    user_id = "6b10a16e02e711e8ae5900163e990bdb"
    description = "A tale of two cities"

    event.build_event(user_id, description)

    assert event.body["event_id"] != ""

def test_should_build_event_with_all_fields(event):
    user_id = "6b10a16e02e711e8ae5900163e990bdb"
    description = "A tale of two cities"

    event.build_event(user_id, description)

    assert event.body["event_id"] != ""
    assert event.body["user_id"] == user_id
    assert event.body["description"] == description
    assert event.body["status"] == "in queue"

def test_should_update_event_status(event):
    event.update_status("processed")
    expected = "processed"

    assert event.body["status"] == expected
