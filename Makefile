containers-start:
	docker-compose up

consumer-up:
	poetry run python3 consumer/main.py

run-api:
	poetry run uvicorn app.main:app --reload

unit-tests:
	poetry run pytest

