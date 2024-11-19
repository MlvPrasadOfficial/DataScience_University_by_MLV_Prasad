import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    df = product.merge(sales,how="inner",left_on="product_id",right_on="product_id")
    q1 = df[(df["sale_date"] >= "2019-01-01") & (df["sale_date"] <= "2019-03-31")] # 1 2    
    notq1 = df[(df["sale_date"] <"2019-01-01") | (df["sale_date"] > "2019-03-31")] # 2 3  
    return df[(df["product_id"].isin(q1["product_id"])) & (~df["product_id"].isin(notq1["product_id"]))][["product_id","product_name"]].drop_duplicates()