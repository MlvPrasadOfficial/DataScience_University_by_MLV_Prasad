import pandas as pd

def count_followers(followers: pd.DataFrame) -> pd.DataFrame:
    

    df = followers.groupby("user_id")["follower_id"].count().reset_index()

    return df.rename(columns = {"follower_id" : "followers_count"})