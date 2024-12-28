from fastapi import APIRouter, HTTPException
import pandas as pd
from database.database import get_connection

router = APIRouter()

@router.get('/')
async def test_api():
    return {
        "message": "Hello World!"
    }
    
@router.get("/total-revenue")
async def total_revenue():
    with get_connection() as connection:
        df = pd.read_sql("SELECT * FROM sales", connection)