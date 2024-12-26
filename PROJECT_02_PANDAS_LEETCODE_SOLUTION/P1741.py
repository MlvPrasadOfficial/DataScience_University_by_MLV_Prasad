import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:    
    df = employees
    df["total_time"] = df["out_time"] - df["in_time"]
    df = df.groupby(["emp_id","event_day"])["total_time"].sum().reset_index()
    return df[["event_day","emp_id","total_time"]].rename(columns= {"event_day" :"day"})