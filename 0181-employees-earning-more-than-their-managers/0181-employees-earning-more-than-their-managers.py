import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(right = employee, how = 'inner', left_on = 'managerId', right_on = 'id')
    return pd.DataFrame(df[df['salary_x'] > df['salary_y']]['name_x']).rename(columns = {'name_x': 'Employee'})
    