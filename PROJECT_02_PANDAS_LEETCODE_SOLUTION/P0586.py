import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    

    # step - 1
    df = orders.groupby(by="customer_number").size().reset_index(name="ct")
    # step - 2
    return df.sort_values("ct",ascending=False).head(1)[["customer_number"]]