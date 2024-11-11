import pandas as pd

def acceptance_rate(friend_request: pd.DataFrame, request_accepted: pd.DataFrame) -> pd.DataFrame:
    

    a =  request_accepted.groupby(["requester_id","accepter_id"]).size().reset_index().shape[0]

    b =  friend_request.groupby(["sender_id","send_to_id"]).size().reset_index().shape[0]


    if b != 0 :
        ans = [round(a/b,2)]
    else :
        ans = [0]

    return pd.DataFrame(data = {"accept_rate"  : ans })