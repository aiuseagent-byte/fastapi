from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def list_clients():
    return [
        {
            "id": 1,
            "name": "Alexandre Martins"
        }
    ]