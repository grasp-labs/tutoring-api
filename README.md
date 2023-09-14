# API
Tiny mock API to demonstrate how we can talk to back-end
applications from client systems.

## Install & run server
1. Clone github repo to local machine (google it)
2. Install python 3.8 & pipenv (google it)
3. Open a terminal & cd into src directory

call 
````commandline
pipenv install

pipenv run uvicorn api.main:app --reload --port 8008
````

## Routes
Api endpoints supported by service

### Arithmatic
Endpoint for a client system to perform mathematical operations.

### Http
Basic routes returning http request header/body
