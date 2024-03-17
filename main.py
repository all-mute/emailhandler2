import json

from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
import os
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

app = FastAPI()

# Разрешить все домены
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # В продакшене лучше указать конкретные домены
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Item(BaseModel):
    text: str

@app.post("/save-text")
async def save_text(item: Request):
    try:
        data = await item.json()
        print(data)
        with open("saved_texts.txt", "a") as file:
            file.write(str(data['email']) + " when: " + str(datetime.now()) + "\n")
        return 200
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5005)

