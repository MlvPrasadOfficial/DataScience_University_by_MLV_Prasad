import pandas as pd

def find_employees(employees: pd.DataFrame) -> pd.DataFrame:
    



    df = employees[~employees["manager_id"].isin(employees["employee_id"]) & (~employees["manager_id"].isnull()) & (employees["salary"] < 30000)]

    return df[["employee_id"]].sort_values("employee_id")