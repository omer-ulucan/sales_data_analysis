import pandas as pd
import numpy

df = pd.read_csv(r"C:\Users\gerha\OneDrive\Desktop\sales_data_analysis\sales_data_analysis\sales_data_set\sales_data_sample.csv", encoding='latin1')
#df is ready, need encoding because the file raised an error

def clean_data(df):
    df["STATE"] = df["STATE"].fillna("N/A")
    df["POSTALCODE"] = df["POSTALCODE"].fillna("N/A")
    df["TERRITORY"] = df["TERRITORY"].fillna("N/A")
    df['FULL_ADDRESS'] = df['ADDRESSLINE1'].fillna('') + " " + df['ADDRESSLINE2'].fillna('')
    df['PRICEEACH'].fillna(df['PRICEEACH'].mean(), inplace=True)
    df['QUANTITYORDERED'].fillna(0, inplace=True)
    df['SALES'] = pd.to_numeric(df['SALES'], errors='coerce')  # Converts non-numeric to NaN

    return df

cleaned_data = clean_data(df)

def total_sales(df):
    return df["SALES"].sum() #in dollars

def cancelled_sales_count(df):
    # Check if 'STATUS' column exists
    if "STATUS" in df.columns:
        # Filter rows where STATUS is 'Cancelled' and count them
        cancelled_count = df["STATUS"].value_counts().get("Cancelled", 0)
        return cancelled_count
    else:
        raise KeyError("Column 'STATUS' is missing in the DataFrame.")


def cancelled_sales_sum(df):
    # Check if "STATUS" Column exists
    if "STATUS" in df.columns and "SALES" in df.columns:
        return df.loc[df["STATUS"] == "Cancelled", "SALES"].sum()
    else:
        raise KeyError("Column 'STATUS' is missing in the DataFrame.")

def country_count(df):
    # Ensure that 'Country' column exists in the DataFrame
    if "COUNTRY" in df.columns:
        # Normalize the 'Country' column to lowercase
        df["COUNTRY"] = df["COUNTRY"].str.lower()
        # Return the count of occurrences for each country
        return df.groupby("COUNTRY").size()
    else:
        raise KeyError("Column 'Country' is missing in the DataFrame.")


def sales_by_country(df, country):
    # Ensure that 'COUNTRY' and 'SALES' columns exist in the DataFrame
    if "COUNTRY" in df.columns and "SALES" in df.columns:
        # Normalize the 'COUNTRY' column to lowercase
        df["COUNTRY"] = df["COUNTRY"].str.lower()
        # Group by the normalized country and calculate the sum of sales
        sales = df.groupby("COUNTRY")["SALES"].sum().reset_index()

        # Check if the provided country is in the 'COUNTRY' column
        country = country.lower()  # Normalize the input country
        if country in sales["COUNTRY"].values:
            return sales[sales["COUNTRY"] == country]
        else:
            raise ValueError(f"Country '{country}' not found in the dataset.")
    else:
        raise KeyError("Columns 'COUNTRY' or 'SALES' are missing in the DataFrame.")

def sales_by_customer(df, customer):
    #ensure that 'CUSTOMERNAME' and 'SALES' columns exist in the DataFrame
    if "CUSTOMERNAME" in df.columns and 'SALES' in df.columns:
        #normalize customername column
        df["CUSTOMERNAME"] = df["CUSTOMERNAME"].str.lower()
        #group by customername
        sales = df.groupby("CUSTOMERNAME")["SALES"].sum().reset_index()

        customer = customer.lower()
        if customer in sales["CUSTOMERNAME"].values:
            return sales[sales["CUSTOMERNAME"] == customer]
        else:
            raise ValueError(f"Customer '{customer}' not found in the dataset.")
    else:
        raise KeyError("Columns 'CUSTOMERNAME' or 'SALES' are missing in the DataFrame")


def monthly_sales(df):
    df["ORDERDATE"] = pd.to_datetime(df["ORDERDATE"], errors ="coerce")
    # Extract Year and Month from the 'ORDERDATE'
    df['YearMonth'] = df['ORDERDATE'].dt.to_period('M')

    monthly_sales = df.groupby("YearMonth")["SALES"].sum().reset_index()
    return monthly_sales

def monthly_sales_by_customer(df, customer):
    customer_sales = monthly_sales(df)
    customer_sales = customer_sales[customer_sales['CUSTOMERNAME'].str.lower() == customer.lower()]
    return customer_sales


