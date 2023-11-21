from fastapi import APIRouter
from pydantic import BaseModel
from typing import Union

from starlette import status
from starlette.responses import JSONResponse

router = APIRouter()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool,None] = None


@router.get("/ping/")
async def ping():
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"message": "pong"}
    )


@router.get("/{item_id}/")
def get_item(item_id: int):
    return {
        "data": {
            "id": item_id,
            "name": f"foobar_{item_id}"
        }
    }


@router.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}



