import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:


    # step -1
    activity["rk"]  = activity.groupby(by="player_id")["event_date"].rank(method="dense")
    # step - 2
    # ste[ - 3]
    
    return activity[activity["rk"] == 1][["player_id","device_id"]]

