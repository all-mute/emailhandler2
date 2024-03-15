from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os

app = FastAPI()

class Item(BaseModel):
    text: str

@app.post("/save-text")
async def save_text(item: Item):
    try:
        with open("saved_texts.txt", "a") as file:
            file.write(item.text + "\n")
        return {"message": "Text saved successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

