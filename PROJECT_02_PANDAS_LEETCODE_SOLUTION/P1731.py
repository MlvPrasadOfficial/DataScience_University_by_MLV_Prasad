import pandas as pd

def count_employees(employees: pd.DataFrame) -> pd.DataFrame:
    


    df = employees.groupby("reports_to").agg(ct = ("reports_to","size"),ag=("age","mean")).reset_index()
    new = df.merge(employees,how="inner",left_on="reports_to",right_on="employee_id")
    new["ag"] = round(new["ag"] + 0.00000000000001,0)
    return new[["employee_id","name","ct","ag"]].rename(columns = {"ct" : "reports_count","ag" : "average_age"})

 