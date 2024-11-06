import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    a = employee
    b = employee


    df = a.merge(b, how= "inner",left_on ="managerId",right_on ="id")
    df = df[df["salary_x"] > df["salary_y"]]
    return df[["name_x"]].rename(columns={"name_x":"Employee"})
    