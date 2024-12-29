from fastapi import FastAPI
from apis.sales import router as sales_router

app = FastAPI()

app.include_router(sales_router, prefix="/sales", tags=["Sales"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Sales Analysis API"}
