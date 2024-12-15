import pandas as pd

def account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    

    df = users.merge(transactions , how = "inner" ,left_on="account", right_on = "account")


    df  = df.groupby(["account","name"])["amount"].sum().reset_index()

    df = df[df["amount"] > 10000]

    return df[["name","amount"]].rename(columns = {"name" : "NAME", "amount" : "BALANCE"})