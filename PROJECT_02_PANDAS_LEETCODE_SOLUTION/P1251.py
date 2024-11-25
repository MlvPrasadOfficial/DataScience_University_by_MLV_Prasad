import pandas as pd

def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:


    s1 = prices.merge(units_sold, how = "left",left_on = "product_id",right_on="product_id")

    s1 = s1[((s1["purchase_date"] >= s1["start_date"])  & (s1["purchase_date"] <= s1["end_date"]) ) | (s1["purchase_date"].isnull()  )]

    s1["revenue"] = s1["price"] *s1["units"]
    s1["units"] = s1["units"].fillna(1000)

    s2 =  s1.groupby("product_id").agg({"units":"sum","revenue":"sum"}).reset_index()

    
    s2["average_price"] = round(s2["revenue"] / s2["units"],2)
    s2 =  s2[["product_id","average_price"]]
    
    return s2

