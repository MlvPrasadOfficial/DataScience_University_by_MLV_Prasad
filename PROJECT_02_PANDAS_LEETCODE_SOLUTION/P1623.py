import pandas as pd
def find_valid_triplets(school_a: pd.DataFrame, school_b: pd.DataFrame, school_c: pd.DataFrame) -> pd.DataFrame:  
    t1 = school_a.merge(school_b , how = "cross")
    t2 = t1.merge(school_c, how="cross")
    t2 = t2[((t2["student_id_x"] != t2["student_id_y"]) & (t2["student_id_y"] != t2["student_id"]) & (t2["student_id"] != t2["student_id_x"]) ) & ((t2["student_name_x"] != t2["student_name_y"]) & (t2["student_name_y"] != t2["student_name"]) & (t2["student_name"] != t2["student_name_x"]) )]
    return t2[["student_name_x","student_name_y","student_name"]].rename(columns = {"student_name_x" : "member_A" , "student_name_y" : "member_B", "student_name" : "member_C"})