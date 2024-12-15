import pandas as pd

def sellers_with_no_sales(customer: pd.DataFrame, orders: pd.DataFrame, seller: pd.DataFrame) -> pd.DataFrame:
    

    orders = orders[orders["sale_date"].dt.year == 2020]


    seller = seller[~seller["seller_id"].isin(orders["seller_id"])]


    return seller[["seller_name"]].rename(columns = {"seller_name" : "SELLER_NAME"}).sort_values("SELLER_NAME")