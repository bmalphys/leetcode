import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    return employee_uni.merge(employees, how = 'right').drop('id', axis = 1)
    