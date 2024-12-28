import pandas as pd
import numpy

df = pd.read_csv(r"C:\Users\gerha\OneDrive\Desktop\sales_data_analysis\sales_data_analysis\sales_data_set\sales_data_sample.csv", encoding='latin1')
#df is ready, need encoding because the file raised an error

def clean_data(df):
    df["ADDRESSLINE2"] = df["ADDRESSLINE2"].fillna("N/A")
    df["STATE"] = df["STATE"].fillna("N/A")
    df["POSTALCODE"] = df["POSTALCODE"].fillna("N/A")
    df["TERRITORY"] = df["TERRITORY"].fillna("N/A")
    #df['PRICEEACH'].fillna(df['PRICEEACH'].mean(), inplace=True)
    #df['QUANTITYORDERED'].fillna(0, inplace=True)
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
            raise ValueError(f"COUNTRY '{country}' not found in the dataset.")
    else:
        raise KeyError("Columns 'COUNTRY' or 'SALES' are missing in the DataFrame.")

