import pandas as pd

def customer_order_frequency(customers: pd.DataFrame, product: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:

    orders["new"] = orders["order_date"].astype(str).str[:7]

    orders = orders[orders["new"].isin(["2020-06","2020-07"])]

    df = orders.merge(product, how ="inner",left_on="product_id",right_on="product_id")

    df["purchase"] = df["quantity"] * df["price"]

    ans = df.merge(customers,how="inner",left_on="customer_id",right_on="customer_id")

    ans = ans.groupby(["customer_id","name","new"])["purchase"].sum().reset_index()

    ans = ans[ans["purchase"] >= 100]

    ans =  ans.groupby(["customer_id","name"]).size().reset_index(name="ct") 

    ans = ans[ans["ct"] == 2]

    return ans[["customer_id","name"]]     