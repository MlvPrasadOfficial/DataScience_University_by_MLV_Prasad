import pandas as pd

def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:


    a = activity[activity["activity_type"] == "start"]
    b = activity[activity["activity_type"] == "end"]


    df = a.merge(b, how = "inner" , on = ["machine_id","process_id"])

    df["processing_time"] = df["timestamp_y"] - df["timestamp_x"]
    df =  df.groupby("machine_id")["processing_time"].mean().reset_index()
    df["processing_time"]  = round(df["processing_time"],3)

    return df