def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    # s1
    person =  person.groupby("email").size().reset_index(name="mlv")
    return person[person["mlv"] > 1][["email"]]
    