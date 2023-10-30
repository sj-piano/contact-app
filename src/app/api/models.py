from pydantic import BaseModel, Field, validator


class ContactSchema(BaseModel):
    name: str = Field(..., min_length=3, max_length=256)
    phone: str = Field(..., min_length=9, max_length=50)
    email: str = Field(..., min_length=6, max_length=256)

    @validator("phone")
    def validate_phone_digits(cls, phone):
        if not phone.isdigit():
            raise ValueError("Phone number must only contain digits")
        return phone


class ContactDB(ContactSchema):
    id: int
