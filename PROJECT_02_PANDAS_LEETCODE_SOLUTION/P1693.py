import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    

    df = daily_sales.groupby(["date_id","make_name"]).nunique().reset_index()

    return df.rename(columns = {"lead_id" : "unique_leads","partner_id" : "unique_partners"})