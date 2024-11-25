import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    imm = delivery[delivery["order_date"]== delivery["customer_pref_delivery_date"]]
    a =  imm.shape[0]
    b = delivery.shape[0]
    ratio = round(100*a/b,2)
    return pd.DataFrame(data = {"immediate_percentage" : [ratio]})


    