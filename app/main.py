# import uvicorn
from fastapi import FastAPI
from .services.route import llama_router

app = FastAPI()
app.include_router(llama_router)

@app.get("/")
async def root():
    return { "message": "Hello World" }

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)
    