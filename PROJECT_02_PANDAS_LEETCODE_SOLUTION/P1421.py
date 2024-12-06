import pandas as pd

def npv_queries(npv: pd.DataFrame, queries: pd.DataFrame) -> pd.DataFrame:


    df = queries.merge(npv, how ="left",left_on=["id","year"],right_on=["id","year"])


    return df.fillna(0)
    