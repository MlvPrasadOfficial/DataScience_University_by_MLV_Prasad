import pandas as pd

def reformat_table(department: pd.DataFrame) -> pd.DataFrame:


    df = pd.pivot(data = department,index = "id", columns = "month", values = "revenue").add_suffix("_Revenue").reset_index()

    df = df.reindex(columns =["id","Jan_Revenue" , "Feb_Revenue", "Mar_Revenue" , "Apr_Revenue", "May_Revenue", "Jun_Revenue" ,"Jul_Revenue", "Aug_Revenue","Sep_Revenue", "Oct_Revenue", "Nov_Revenue" , "Dec_Revenue" ])

    return df
    


    