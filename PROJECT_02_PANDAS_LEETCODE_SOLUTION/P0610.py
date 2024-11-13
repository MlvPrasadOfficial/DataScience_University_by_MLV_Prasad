import pandas as pd

def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:



    def logic(t) :
        if ( t.x + t.y > t.z ) & ( t.y + t.z > t.x ) & ( t.z  + t.x > t.y  ) :
            return "Yes"
        else :
            return "No"

    triangle["triangle"]   = triangle.apply(lambda t : logic(t) ,axis = 1)

    return triangle
    