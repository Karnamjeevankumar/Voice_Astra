from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class question(BaseModel):
    question: str
@app.post("/ask")
async def ask(question: question):
    return{
        "message": question.question
    }