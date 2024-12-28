from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get('/')
async def test():
    return {"message": "Hello World!"}