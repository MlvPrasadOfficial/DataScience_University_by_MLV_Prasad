import pandas as pd

def ad_free_sessions(playback: pd.DataFrame, ads: pd.DataFrame) -> pd.DataFrame:
    

    df = playback.merge(ads, how="inner",on ="customer_id")


    df =  df[((df["timestamp"] >= df["start_time"] )  & (df["timestamp"]<= df["end_time"]))][["session_id"]].drop_duplicates()


    return playback[~playback["session_id"].isin(df["session_id"])][["session_id"]]