import pandas as pd

def ads_performance(ads: pd.DataFrame) -> pd.DataFrame:



    df =  ads.groupby("ad_id").apply(lambda i :   np.round(100*(i["action"]=="Clicked").sum()/(i["action"]!="Ignored").sum(),2) ).reset_index(name = "ctr").fillna(0)

    return df.sort_values(["ctr","ad_id"],ascending=[False,True])
    