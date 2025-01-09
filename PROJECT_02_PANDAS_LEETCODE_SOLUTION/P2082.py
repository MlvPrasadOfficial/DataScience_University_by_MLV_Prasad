import pandas as pd

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    value = store[store["amount"] > 500]["customer_id"].nunique()
    ans = pd.DataFrame(data =  {"rich_count" : [value] })

    return ans 