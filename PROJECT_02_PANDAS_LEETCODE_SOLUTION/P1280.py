import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:

    s1 = students.merge(subjects,how="cross")
    s2 = examinations.groupby(["student_id","subject_name"]).size().reset_index(name ="attended_exams")
    s3 = s1.merge(s2,how="left",left_on =["student_id","subject_name"],right_on=["student_id","subject_name"])
    s3["attended_exams"].fillna(0,inplace=True)
    return s3.sort_values(["student_id","subject_name"])
    