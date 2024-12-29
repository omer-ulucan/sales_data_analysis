# Sales Data Analysis API

## Contributors

- **Sinan Can Demir** ([eisensenpou](https://github.com/eisensenpou))
- **Ömer Ulucan** ([omer-ulucan](https://github.com/omer-ulucan))

## Overview

This project provides a RESTful API for analyzing sales data from a CSV file using **FastAPI**, **SQLite**, and **Pandas**. It includes functionality for data cleaning, analysis, and database management. The backend is designed to process sales data and provide insights through API endpoints.

## Features

- Clean raw sales data using predefined rules.
- Analyze data for:
  - Total sales.
  - Net sales (after cancellations).
  - Count and sum of canceled sales.
  - Sales grouped by country or customer.
  - Monthly sales breakdown.
- Store sales data and analysis results in SQLite.
- Easy integration and modular design.

## Project Structure

```
project/
├── data_analysis/analysis.py              # Data cleaning and analysis functions
├── database/
│   ├── database.py          # SQLite connection manager
│   ├── create_table.py      # Database schema creation
│   ├── insert_data.py       # Insert data into the database
│   ├── query_data.py        # Query analysis results from the database
├── apis/
│   ├── sales.py             # API endpoints for sales data analysis
├── main.py                  # Entry point for FastAPI application
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

## Prerequisites

- Python 3.8+
- SQLite

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/sales-data-analysis-api.git
   cd sales-data-analysis-api
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up the database:

   ```bash
   python database/create_table.py
   ```

4. Insert data into the database:

   ```bash
   python database/insert_data.py
   ```

## Usage

### Start the FastAPI Server

Run the application locally:

```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

### API Endpoints

#### Sales Analysis

| Endpoint                        | Method | Description                            |
| ------------------------------- | ------ | -------------------------------------- |
| `/sales/total-sales/`           | GET    | Returns the total sales amount.        |
| `/sales/net-sales/`             | GET    | Returns the net sales amount.          |
| `/sales/cancelled-sales/count/` | GET    | Returns the count of canceled sales.   |
| `/sales/cancelled-sales/sum/`   | GET    | Returns the sum of canceled sales.     |
| `/sales/sales-by-country/`      | GET    | Returns sales for a specific country.  |
| `/sales/sales-by-customer/`     | GET    | Returns sales for a specific customer. |
| `/sales/monthly-sales/`         | GET    | Returns sales data grouped by month.   |

### Example API Call

Fetch total sales:

```bash
curl -X GET http://127.0.0.1:8000/sales/total-sales/
```

Response:

```json
{
  "total_sales": 12345.67
}
```

## Development

### Testing the API

To test the API, use tools like:

- [Postman](https://www.postman.com/)
- [cURL](https://curl.se/)

### Adding New Features

1. Add analysis logic in `analysis.py`.
2. Add corresponding database queries in `query_data.py`.
3. Create an API endpoint in `apis/sales.py`.

### Future Improvements

- Add user authentication with JWT tokens.
- Integrate a frontend for data visualization.
- Expand analysis features (e.g., predictive models).

