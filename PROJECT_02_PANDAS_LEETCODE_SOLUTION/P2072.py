import pandas as pd

def find_winner(new_york: pd.DataFrame, california: pd.DataFrame) -> pd.DataFrame:
    n = len(new_york[new_york["score"] >= 90])
    c = len(california[california["score"] >= 90]) 
    if n > c  :
        ans = "New York University"
    elif n < c :
        ans = "California University"
    else :
        ans = "No Winner"

    return pd.DataFrame(data = {"winner" : [ans]})
    