import pandas as pd
from datetime import datetime

def find_valid_users(purchases: pd.DataFrame, start_date: datetime, end_date: datetime, min_amount: int) -> pd.DataFrame:
    

    purchases = purchases[ ( purchases["time_stamp"] >= start_date) & ( purchases["time_stamp"] <=end_date) & ( purchases["amount"] >= min_amount)]


    return purchases[["user_id"]].drop_duplicates().sort_values("user_id")