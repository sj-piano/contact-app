# Imports
from fastapi import APIRouter, HTTPException
from typing import List


# Local imports
from app.api import crud
from app.api.models import ContactDB, ContactSchema


# Setup
router = APIRouter()


@router.post("/", response_model=ContactDB, status_code=201)
async def create_contact(payload: ContactSchema):
    contact_id = await crud.post(payload)

    response_object = {
        "id": contact_id,
        "name": payload.name,
        "phone": payload.phone,
        "email": payload.email,
    }
    return response_object


@router.get("/{id}/", response_model=ContactDB)
async def read_contact(id: int):
    contact = await crud.get(id)
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact


@router.get("/", response_model=List[ContactDB])
async def read_all_contacts():
    return await crud.get_all()


@router.put("/{id}/", response_model=ContactDB)
async def update_contact(id: int, payload: ContactSchema):
    contact = await crud.get(id)
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")

    contact_id = await crud.put(id, payload)

    response_object = {
        "id": contact_id,
        "name": payload.name,
        "phone": payload.phone,
        "email": payload.email,
    }
    return response_object
