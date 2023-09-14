# API
Tiny mock API to demonstrate how we can talk to back-end
applications from client systems.

## Run server
CD into src

call 
````commandline
pipenv install

pipenv run uvicorn api.main:app --reload --port 8008
````

## Routes
Api endpoints supported by service

### Arithmatic
Endpoint for a client system to perform mathematical operations.
