from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    """根路径，返回欢迎信息"""
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q:str | None = None):
    """根据item_id获取物品信息，可选查询参数q"""
    return {"item_id": item_id, "q": q} 