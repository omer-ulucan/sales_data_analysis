from fastapi import APIRouter, HTTPException
import pandas as pd
from database.query_data import *
from data_analysis.analysis import *
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
    
@router.get("/net-sales/")
async def get_net_sales():
    try:
        with  get_connection() as connection:
            df = pd.read_sql("SQL * FROM sales", connection)
        net = net_sales(df)
        return {"net_sales": net}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error calculating net sales: {e}")
    
@router.get("/canceled-sales/count/")
async def calculate_cancelled_sales_count():
    try:
        with get_connection() as connection:
            df = pd.read_sql("SELECT * FROM sales", connection)
        
        count = cancelled_sales_count(df)
        insert_analysis_result("Cancelled Sales Count", count)
        return {"cancelled_sales_count": count}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error calculating cancelled sales count: {e}")

@router.get("/cancelled-sales/sum")
async def get_cancelled_sales_sum():
    try:
        with get_connection() as connection:
            df = pd.read_sql("SELECT * FROM sales", connection)
        total = cancelled_sales_count(df)
        return {"cancelled_sales_sum": total}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error calculating cancelled sales sum: {e}")

@router.get("/sales-by-country/")
async def get_sales_by_country(country: str):
    """
    Get total sales for a specific country
    """
    try:
        with get_connection() as connection:
            df = pd.read_sql("SELECT * FROM sales", connection)
        sales = sales_by_country(df, country)
        return sales.to_dict(orient="records")
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving sales by country: {e}")

@router.get("/sales-by-customer/")
async def get_sales_by_customer(customer: str):
    """
    Get total sales for a specific customer
    """
    try:
        with get_connection() as connection:
            df = pd.read_sql("SELECT * FROM sales", connection)
        sales = sales_by_customer(df, customer)
        return sales.to_dict(orient="records")
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving sales by customer: {e}")

@router.get("/monthly-sales/")
async def get_monthly_sales():
    """
    Get monthly sales totals
    """
    try:
        with get_connection() as connection:
            df = pd.read_sql("SELECT * FROM sales", connection)
        monthly = monthly_sales(df)
        return monthly.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving monthly sales: {e}")

@router.get("/analysis-results/")
async def fetch_analysis_results():
    try:
        results = get_analysis_result()
        return {"analysis_results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching analysis results: {e}")