import pandas as pd

def unique_orders_and_customers(orders: pd.DataFrame) -> pd.DataFrame:

    orders = orders[orders["invoice"] > 20]


    orders["month"] = orders["order_date"].astype(str).str[:7]

    return orders.groupby("month").agg(order_count = ("order_id","nunique"), customer_count=("customer_id","nunique")).reset_index()