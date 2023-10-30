# Local imports
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


async def put(id: int, payload: ContactSchema):
    query = (
        contacts
        .update()
        .where(id == contacts.c.id)
        .values(name=payload.name, phone=payload.phone, email=payload.email)
        .returning(contacts.c.id)
    )
    return await database.execute(query=query)


async def delete(id: int):
    query = contacts.delete().where(id == contacts.c.id)
    return await database.execute(query=query)
