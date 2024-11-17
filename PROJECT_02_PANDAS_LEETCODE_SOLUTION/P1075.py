import pandas as pd

def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:


    df = project.merge(employee,how="inner",left_on = "employee_id",right_on ="employee_id")
    df =  df.groupby("project_id")["experience_years"].mean().reset_index(name="average_years")    
    df["average_years"] = round(df["average_years"],2)
    return df