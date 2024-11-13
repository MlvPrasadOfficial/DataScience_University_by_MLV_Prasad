import pandas as pd
import numpy as np
def shortest_distance(point: pd.DataFrame) -> pd.DataFrame:


    a = point.copy()
    b = point.copy()
    df = a.merge(b,how="cross")

    df = df[df["x_x"] != df["x_y"]]

    df["distance"] = abs(df["x_x"] - df["x_y"])

    mn = df["distance"].min()

    return pd.DataFrame(data = {  "shortest" : [ mn ]   })

