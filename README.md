## Disclaimers

I wasn't able to make the docker-compose work with all the services. I believe is an issue with my computer (I used to develop in my work's computer
and some settings are not well configured). However, to mitigate the issue, I setup a Makefile.

I've submitted the `.env` file to make execution easier, I know it is not a good practice.

## Requirements
- Python 3.13
- Docker

## Running the application

### Starting containers
`$ make containers-start`

### Running Consumer
`$ make consumer-up`

### Starting API
`$ make run-api`

### Running Tests
`$ unit-tests`

## Making requests

### Send an event
```shell
curl -H 'Content-Type: application/json' \
      -d '{ "user_id":"6b10a16e02e590016990r","description":"A Tale of Two Cities"}' \
      -X POST \
      127.0.0.1:8000/events
```

### Update an Event
```shell
curl -H 'Content-Type: application/json' \
      -d '{"status":"processed"}' \
      -X PATCH \
      127.0.0.1:8000/events/<event_id>
```

### Get an Event
```shell
curl 'http://127.0.0.1:8000/events/<event_id>'
```