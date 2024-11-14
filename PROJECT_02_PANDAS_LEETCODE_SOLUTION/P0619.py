import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:



    df = my_numbers.groupby(by="num").size().reset_index(name="mlv")

    df = df[df["mlv"] == 1]

    mx = df["num"].max()

    return pd.DataFrame(data = {"num" : [mx]})
    