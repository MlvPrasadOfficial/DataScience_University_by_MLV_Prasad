import pandas as pd

def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
    df = register.groupby("contest_id")["user_id"].count().reset_index()
    df["user_id"]  = round(100*df["user_id"] / (users.shape[0]),2)
    return df.rename(columns = {"user_id" : "percentage"}).sort_values(["percentage","contest_id"], ascending = [False,True])
    