from fastapi import FastAPI, APIRouter
from views import items_router

app = FastAPI()

app.include_router(items_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
