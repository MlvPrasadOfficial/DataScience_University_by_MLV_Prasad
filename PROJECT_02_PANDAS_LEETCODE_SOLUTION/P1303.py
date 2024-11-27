import pandas as pd

def team_size(employee: pd.DataFrame) -> pd.DataFrame:

    s1 = employee.groupby("team_id").size().reset_index(name="team_size")


    s2 = s1.merge(employee,how="inner",left_on="team_id",right_on="team_id")

    return s2[["employee_id","team_size"]]
    