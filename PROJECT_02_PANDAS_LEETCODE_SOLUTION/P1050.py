import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:


    df = actor_director.groupby(by=["actor_id","director_id"]).size().reset_index(name = "ctrows")

    df = df[df["ctrows"] >= 3]

    return df[["actor_id","director_id"]]
    