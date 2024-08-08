from fastapi import APIRouter

router = APIRouter()

@router.get("/routers/items")
async def read_items():
    return [{"demo": "in router"}, {"name": "Item Foo"}, {"name": "Item Bar"}]