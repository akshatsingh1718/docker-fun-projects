from fastapi import FastAPI
import uvicorn
from typing import Optional


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str]= None):
    return {"item_id": item_id, "q": q}


if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")
