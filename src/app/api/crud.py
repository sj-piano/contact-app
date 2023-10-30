from app.api.models import ContactSchema
from app.db import contacts, database


async def post(payload: ContactSchema):
    query = contacts.insert().values(name=payload.name, phone=payload.phone, email=payload.email)
    return await database.execute(query=query)


async def get(id: int):
    query = contacts.select().where(id == contacts.c.id)
    return await database.fetch_one(query=query)


async def get_all():
    query = contacts.select()
    return await database.fetch_all(query=query)
