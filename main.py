from typing import Union

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel



app = FastAPI()

class Item(BaseModel):
    item_id: int
    name: str
    price: float
    is_offer: Union[bool, None] = None

items = []

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[int, None] = None):
    for item in items:
        if item.item_id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/item/")
def update_item(item: Item):
    items.append(item)
    return {"item_price": item.price, "item_id": item.item_id}