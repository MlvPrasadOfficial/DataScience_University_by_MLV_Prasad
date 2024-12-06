import pandas as pd

def top_travellers(users: pd.DataFrame, rides: pd.DataFrame) -> pd.DataFrame:


    df = users.merge(rides, how="left", left_on = "id", right_on = "user_id")

    df.fillna(0,inplace=True)

    return df.groupby(["id_x","name"])["distance"].sum().reset_index().rename(columns = {"distance" : "travelled_distance"}).sort_values(["travelled_distance","name"],ascending = [False,True])[["name","travelled_distance"]]
    