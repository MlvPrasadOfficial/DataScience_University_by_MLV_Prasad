import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # step 1

    df = customers.merge(orders, how ="left",left_on ="id", right_on ="customerId")
    #step -2
    

    return df[df["customerId"].isnull()][["name"]].rename(columns= {"name" : "Customers"})