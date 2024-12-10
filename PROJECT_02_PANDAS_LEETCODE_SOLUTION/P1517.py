import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:

    return users[users["mail"].str.match(r"^[A-Za-z][-._a-zA-Z0-9]*@leetcode\.com$")]