import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    

    def logic(i) :
        if i["employee_id"] %2 ==1 and i["name"][0] != "M" :
            return i["salary"]
        else :
            return 0
    employees["bonus"]  = employees.apply(lambda i : logic(i), axis = 1)


    return employees[["employee_id","bonus"]].sort_values("employee_id")