import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    
    #step - 1
    df = employee.merge(bonus,how="left",left_on="empId",right_on="empId")

    # step -2 (null | < 1000)
    return df[(df["bonus"].isnull()) | (df["bonus"] < 1000)][["name","bonus"]]