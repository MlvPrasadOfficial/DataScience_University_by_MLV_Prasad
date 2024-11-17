import pandas as pd

def project_employees_ii(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:  
    df = project.groupby(by='project_id').size().reset_index(name="ctrows")
    mx = df["ctrows"].max()
    df = df[df["ctrows"] == mx]
    return df[["project_id"]]