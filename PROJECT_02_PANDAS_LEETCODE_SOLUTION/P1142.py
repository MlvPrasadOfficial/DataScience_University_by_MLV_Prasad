import pandas as pd

def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    

    df = activity[(activity["activity_date"] >= "2019-06-28") & (activity["activity_date"] <= "2019-07-27")]


    num = df["session_id"].nunique()
    den = df["user_id"].nunique()

    if den == 0 :
        ratio = 0
    else :
        ratio  = round(num/den,2)
    return pd.DataFrame(data = {"average_sessions_per_user" : [ratio]})