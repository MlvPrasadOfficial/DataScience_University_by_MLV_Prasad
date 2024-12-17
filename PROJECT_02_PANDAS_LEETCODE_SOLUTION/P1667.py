import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:

    users["l"]  = users["name"].str[0]
    users["r"]  = users["name"].str[1:]

    users["name"] = users["l"].str.upper() + users["r"].str.lower()


    return users[["user_id","name"]].sort_values("user_id")
    
    