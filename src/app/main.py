# Imports
from fastapi import FastAPI


# Local imports
from app.api import contacts, ping
from app.db import engine, database, metadata


# Setup
metadata.create_all(engine)
app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(ping.router)
app.include_router(contacts.router, prefix="/contacts", tags=["contacts"])
