from fastapi import APIRouter
from pydantic import BaseModel
# from .llama import Llama27bModel

llama_router = APIRouter()
# llm = Llama27bModel()

class Question(BaseModel):
    question: str
   
@llama_router.post("/llama", tags=["Llama"])
async def llama(payload: Question):
    # output = llm.get_output(payload.question)
    # print(payload)
    return f'Answer of this question is this: {payload.question}'
