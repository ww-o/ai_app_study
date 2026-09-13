from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.post("/items")
def create_item(item: Item):
    """创建新商品，接收 JSON 请求体"""
    return item

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    """更新指定商品，同时使用路径参数和请求体"""
    return {"item_id": item_id, "item_name": item.name}