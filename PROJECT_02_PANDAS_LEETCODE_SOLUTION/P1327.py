import pandas as pd

def list_products(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    

    df = products.merge(orders, how="inner",left_on="product_id",right_on="product_id")

    df = df[(df["order_date"].dt.month == 2) & (df["order_date"].dt.year == 2020)]


    df = df.groupby("product_name")["unit"].sum().reset_index()

    return df[df["unit"] >= 100]