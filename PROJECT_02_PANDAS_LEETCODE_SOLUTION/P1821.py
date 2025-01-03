import pandas as pd

def find_customers(customers: pd.DataFrame) -> pd.DataFrame:    
    df = customers
    return df[(df["year"]  == 2021  ) & (df["revenue"] > 0 )][["customer_id"]]