import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:



    df = product.merge(sales,how="inner",left_on="product_id",right_on="product_id")

    s8 = df[df["product_name"]=="S8"][["buyer_id"]]
    iphn = df[df["product_name"]=="iPhone"][["buyer_id"]]


    s8 =  s8[~s8["buyer_id"].isin(iphn["buyer_id"])]

    return s8.drop_duplicates()


    