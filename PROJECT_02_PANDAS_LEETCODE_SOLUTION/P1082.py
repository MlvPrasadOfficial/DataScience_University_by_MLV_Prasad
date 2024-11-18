import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    

    df = sales.groupby(by="seller_id")["price"].sum().reset_index()

    mx = df["price"].max()

    df = df[df["price"] == mx]

    return df[["seller_id"]]