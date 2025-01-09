import pandas as pd
from datetime import datetime

def count_valid_users(purchases: pd.DataFrame, start_date: datetime, end_date: datetime, min_amount: int) -> pd.DataFrame:
    

    df = purchases[(purchases["time_stamp"]  >= start_date)  &  (purchases["time_stamp"] <= end_date)]
    df = df[df["amount"] >= min_amount]
    ans = df["user_id"].nunique()
    return pd.DataFrame(data = {"user_cnt" : [ ans]})