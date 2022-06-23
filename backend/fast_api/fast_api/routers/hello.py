from fastapi import APIRouter

router = APIRouter(tags=["Test"], prefix="/test")


@router.get("")
async def test():
    return {"message": "Hello World"}
