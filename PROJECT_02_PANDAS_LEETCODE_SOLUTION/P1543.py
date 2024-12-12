import pandas as pd
def fix_name_format(sales: pd.DataFrame) -> pd.DataFrame:
    sales["product_name"] = sales["product_name"].str.lower().str.strip()
    sales["sale_date"] = sales["sale_date"].astype(str).str[:7]
    sales = sales.groupby(["product_name","sale_date"]).size().reset_index(name="total")
    return sales
    