import pandas as pd

def find_requesting_users(signups: pd.DataFrame, confirmations: pd.DataFrame) -> pd.DataFrame:
    
    confirmations = confirmations.sort_values(["user_id","time_stamp"])
    confirmations["new_date"] = confirmations.groupby(["user_id"])["time_stamp"].shift(1)
    confirmations["diff"] =  confirmations["time_stamp"] -   confirmations["new_date"]
    confirmations = confirmations[confirmations["diff"].notna()]
    confirmations["diff"] = confirmations["diff"].astype(int)
    # return confirmations
    confirmations = confirmations[confirmations["diff"] <= (24* 60*60*1000000000  )]
    return confirmations[["user_id"]].drop_duplicates()