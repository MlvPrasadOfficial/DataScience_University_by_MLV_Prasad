import pandas as pd

def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    

    ct = employee.groupby("employee_id").size().reset_index(name = "ctrows")

    df = ct.merge(employee, how="inner", on = "employee_id")
    return  df[(df["ctrows"] == 1 ) | (df["primary_flag"] == "Y")][["employee_id","department_id"]]