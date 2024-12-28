import pandas as pd
import numpy

df = pd.read_csv(r"C:\Users\gerha\OneDrive\Desktop\sales_data_analysis\sales_data_analysis\sales_data_set\sales_data_sample.csv", encoding='latin1')
#df is ready, need encoding because the file raised an error

def cleaning():
    df["ADDRESSLINE2"] = df["ADDRESSLINE2"].fillna("N/A")
    df["STATE"] = df["STATE"].fillna("N/A")
    df["POSTALCODE"] = df["POSTALCODE"].fillna("N/A")
    df["TERRITORY"] = df["TERRITORY"].fillna("N/A")

#cleaning()
df.isnull().sum()