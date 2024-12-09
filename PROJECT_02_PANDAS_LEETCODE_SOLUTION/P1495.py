import pandas as pd

def friendly_movies(tv_program: pd.DataFrame, content: pd.DataFrame) -> pd.DataFrame:

    a = content[ ( content["Kids_content"] == "Y")   & (content["content_type"]=="Movies")]
    a["content_id"] = a["content_id"].astype(int)
    b = tv_program[(tv_program["program_date"].dt.year == 2020 )  & (tv_program["program_date"].dt.month == 6)]
    df = a.merge(b, how = 'inner', left_on ="content_id", right_on="content_id")
    return df[["title"]].drop_duplicates().rename(columns = {"title" : "TITLE"})
    