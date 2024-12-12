import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    



    visits = visits[~visits["visit_id"].isin(transactions["visit_id"])]
# count(*)
    return visits.groupby("customer_id")["visit_id"].size().reset_index (name="count_no_trans")