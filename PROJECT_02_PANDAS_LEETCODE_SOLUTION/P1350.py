import pandas as pd

def find_students(departments: pd.DataFrame, students: pd.DataFrame) -> pd.DataFrame:


    df = students.merge(departments, how = "left", left_on="department_id",right_on="id")

    return df[df["id_y"].isnull()][["id_x","name_x"]].rename(columns = {"id_x" : "id", "name_x" : "name"})
    