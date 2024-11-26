import pandas as pd

def weather_type(countries: pd.DataFrame, weather: pd.DataFrame) -> pd.DataFrame:
    s1 = weather[(weather["day"].dt.year == 2019) & (weather["day"].dt.month == 11 ) ]

    s2 = s1.groupby("country_id")["weather_state"].mean().reset_index()

    def logic(x):
        if x["weather_state" ] <= 15 :
            return "Cold"
        elif x["weather_state"] >= 25 :
            return "Hot"
        else :
            return "Warm"

    s2["weather_type"] = s2.apply(lambda x : logic(x),axis = 1)

    s3 = countries.merge(s2, how="inner",left_on = "country_id",right_on="country_id")

    return s3[["country_name","weather_type"]]