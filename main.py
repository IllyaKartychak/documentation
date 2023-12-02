from fastapi import FastAPI

from pydantic import BaseModel, Field
app = FastAPI()

class IncomeMessages(BaseModel):
    author: str = Field(examples=["plains", "cars"])
    text: str





@app.get("/", tags=["messages"])
def income_messages() -> IncomeMessages:
    return {"author": "9", "text": "hello"}
