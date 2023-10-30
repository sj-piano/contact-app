from pydantic import BaseModel, Field


class ContactSchema(BaseModel):
    name: str = Field(..., min_length=3, max_length=256)
    phone: str = Field(..., min_length=9, max_length=50)
    email: str = Field(..., min_length=6, max_length=256)


class ContactDB(ContactSchema):
    id: int
