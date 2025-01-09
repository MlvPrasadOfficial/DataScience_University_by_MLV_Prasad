import pandas as pd

def low_quality_problems(problems: pd.DataFrame) -> pd.DataFrame:
    
    df = problems

    return df[(df["likes"]/(df["likes"] + df["dislikes"])) < 0.6][["problem_id"]].sort_values("problem_id")