import pandas as pd

def count_comments(submissions: pd.DataFrame) -> pd.DataFrame:


    submissions = submissions.drop_duplicates()


    s1 = submissions[submissions["parent_id"].isnull()]

    s2 = submissions[submissions["parent_id"].isin(s1["sub_id"])]

    s3 = s2.groupby("parent_id")[["sub_id"]].nunique().reset_index()


    return s1.merge(s3,how="left",left_on="sub_id",right_on="parent_id")[["sub_id_x","sub_id_y"]].fillna(0).rename(columns = {"sub_id_x" : "post_id","sub_id_y" : "number_of_comments"}).sort_values("post_id")
    