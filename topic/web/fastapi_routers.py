from fastapi import APIRouter

router = APIRouter()

@router.get("/routers/items" , tags=["routers"])
async def read_items():
    return [{"demo": "in router"}, {"name": "Item Foo"}, {"name": "Item Bar"}]