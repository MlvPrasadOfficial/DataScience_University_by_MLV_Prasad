import pandas as pd

def consecutive_available_seats(cinema: pd.DataFrame) -> pd.DataFrame:

    cinema.sort_values("seat_id",inplace=True)
    cinema["pf"] = cinema["free"].shift(1)
    cinema["nf"] = cinema["free"].shift(-1)   

    return cinema[ ((cinema["free"]==1) & (cinema["pf"]==1)) |  ((cinema["free"]==1) & (cinema["nf"]==1))  ][["seat_id"]]
    