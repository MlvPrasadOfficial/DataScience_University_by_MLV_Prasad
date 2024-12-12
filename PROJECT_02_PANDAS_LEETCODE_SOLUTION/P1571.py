import pandas as pd

def warehouse_manager(warehouse: pd.DataFrame, products: pd.DataFrame) -> pd.DataFrame:

    df = warehouse.merge(products, how = "inner", left_on = "product_id",right_on="product_id")

    df["volume"] = df["units"] * df["Width"] * df["Length"] * df["Height"]

    return df.groupby("name")["volume"].sum().reset_index().rename(columns = {"name" : "warehouse_name"})
    