from fastapi import APIRouter

router = APIRouter()

@router.get("/fullname/{first_name}/{last_name}")
async def get_full_name(first_name: str, last_name: str):
    full_name = f"{first_name} {last_name}"
    return {"full_name": full_name}
