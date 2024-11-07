import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    a = weather #yesterday
    b = weather # today
    # step 1
    b["previous"] = b["recordDate"] + pd.DateOffset(-1)
    df = a.merge(b,how="inner",left_on="recordDate",right_on="previous")

    # step 2
    df = df[df["temperature_x"]<df["temperature_y"]]
    # step 3

    return df[["id_y"]].rename(columns= {"id_y":"Id"})
    