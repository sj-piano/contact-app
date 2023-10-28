from fastapi import APIRouter

router = APIRouter()


@router.get("/ping")
async def pong():
    # some async operation could happen here
    # example: `contacts = await get_all_contacts()`
    return {"ping": "pong!"}