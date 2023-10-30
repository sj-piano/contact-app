from pydantic import BaseModel


class ContactSchema(BaseModel):
    name: str
    phone: str
    email: str


class ContactDB(ContactSchema):
    id: int
