import pandas as pd

def reported_posts(actions: pd.DataFrame) -> pd.DataFrame:
    #s 1

    actions = actions[(actions["action_date"]=="2019-07-04") & (actions["action"]=="report")][["post_id","extra"]].drop_duplicates()
    return actions.groupby("extra").size().reset_index(name="report_count").rename(columns = {"extra" : "report_reason"})