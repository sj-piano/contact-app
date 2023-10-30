# Project: Contact Database API


## Summary

A Python API that provides CRUD functionality (create, read, update, and delete) for a contact database.

Each contact has a name, phone number, and email address.


## Run this project locally

Clone the repo and change to the repo directory:  
`git clone git@github.com:sj-piano/contact-app.git && cd contact-app`

Copy the template to make a `.env` file. Adjust its values if you prefer not to use the defaults.  
`cp .env.example .env`

Check that your Docker service or desktop app is running.

Build the images and run the containers:  
`docker-compose up -d --build`

The project should now be running.

Quick test: Browse to  
http://localhost:8002/ping

Expected output:  
`{"ping":"pong!"}`

Run all the tests:  
`docker-compose exec api pytest`

Run a single test:  
`docker-compose exec api pytest tests/test_contacts.py::test_create_contact`

Stop the project:  
`docker-compose down`

To stop the project and delete the persistent volume that contains the database:  
`docker-compose down --volumes`


## Use the API

Use the built-in interactive Swagger API by browsing to:  
http://localhost:8002/docs/

List all contacts in the database by browsing to:  
http://localhost:8002/contacts/


## Data input formats

Contact names must be between 3 and 256 characters.

Contact phone numbers must be between 9 and 50 characters, and contain only digits.

Contact email addresses must be between 6 and 256 characters.


## Tech stack

* Docker Compose
* PostgreSQL
* Python 3
* SQLAlchemy ORM
* FastAPI framework
* Uvicorn (ASGI server)
* Pydantic (runtime type validation)
* Flake8 (style checking)


## Additional details

The Swagger UI will return the detailed Pydantic type validation errors.

The tests use mocking to avoid interacting with the database. They only test the routers and methods.

Versions:  
- PostgreSQL 15.1  
- Python 3.11  

The `uvicorn` server startup command uses `--reload` and watches the directory `src` via a Docker volume. This means that changes in the `src` directory will cause the server to reload itself with the new code. (Very useful during development.)
