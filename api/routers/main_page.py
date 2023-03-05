from fastapi import APIRouter

router = APIRouter(
    tags=["Основная страница"],
)


@router.get("/")
async def main_page():
    return {"message": "Hello world"}
