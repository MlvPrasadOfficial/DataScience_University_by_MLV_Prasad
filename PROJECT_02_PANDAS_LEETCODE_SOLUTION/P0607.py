import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:



    df = company.merge(orders, how="inner",left_on="com_id",right_on="com_id")

    df = df[df["name"]=="RED"]

    sales_person = sales_person[~sales_person["sales_id"].isin(df["sales_id"])]

    return sales_person[["name"]]
    