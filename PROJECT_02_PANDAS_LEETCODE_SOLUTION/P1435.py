import pandas as pd

def create_bar_chart(sessions: pd.DataFrame) -> pd.DataFrame:


    return pd.cut(sessions["duration"], bins=[ 0,300,600,900,10000000000000000000000000],labels =["[0-5>","[5-10>","[10-15>","15 or more"]).value_counts().reset_index().rename(columns = {"duration" : "bin", "count" : "total"})
    