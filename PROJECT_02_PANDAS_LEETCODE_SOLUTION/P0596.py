import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:


    # STEP1
    df =  courses.groupby(by="class").size().reset_index(name="ct")

    # step 2
    df = df[df["ct"] >= 5]
    # step 3
    return df[["class"]]
    