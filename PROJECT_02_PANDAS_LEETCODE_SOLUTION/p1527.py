import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    # START WITH DIAB1 OR SPACE + DAIB1


    return patients[patients["conditions"].str.contains(r"(^DIAB1)|( DIAB1)")]