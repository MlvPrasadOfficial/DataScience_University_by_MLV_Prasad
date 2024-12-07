import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:



    df =  activities.groupby("sell_date").agg([("product","nunique"),("product",lambda x   : ",".join(sorted(x.unique())))]).reset_index()

    df.columns = ["sell_date","num_sold","products"]

    return df
    