from fastapi import APIRouter, HTTPException
from database.query_data import insert_analysis_result, get_analysis_results
from data_analysis.analysis import total_sales, cancelled_sales_count, cancelled_sales_sum
from database.database import get_connection

router = APIRouter()
    
@router.get("/total-sales")
async def get_total_sales():
    try:
        with get_connection() as connection:
            df = pd.read_sql("SELECT * FROM sales", connection)
        total = total_sales(df)
        return {"total_sales": total}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error calculation total_sales: {e}")
    
@router.get("/canceled-sales/count/")
async def calculate_cancelled_sales_count():
    try:
        with get_connection() as connection:
            df = pd.read_sql("SELECT * FROM sales", connection)
        
        count = cancelled_sales_count(df)
        insert_analysis_result("Cancelled Sales Count", count)
        return {"cancelled_sales_count": count}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error calculation cancelled sales count: {e}")

@router.get("/analysis-results/")
async def fetch_analysis_results():
    try:
        results = get_analysis_results()
        return {"analysis_results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching analysis results: {e}")