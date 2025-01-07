import pandas as pd

def find_employees(employees: pd.DataFrame, salaries: pd.DataFrame) -> pd.DataFrame:
    df = employees.merge(salaries, how="outer", on="employee_id")
    return df[(df["name"].isna())  |   (df["salary"].isna())][["employee_id"]].sort_values("employee_id")
    