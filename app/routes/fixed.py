from fastapi import APIRouter

router = APIRouter()

@router.get("/api/fixed-endpoint")
async def read_fixed_endpoint():
    return {"message": "This is a fixed endpoint"}