import pandas as pd

def analyze_products(product: pd.DataFrame, invoice: pd.DataFrame) -> pd.DataFrame:

    df = invoice.groupby("product_id").sum().reset_index()
    df = product.merge(df,how="left",on="product_id")
    return df[["name","rest","paid","canceled","refunded"]].sort_values("name").fillna(0)