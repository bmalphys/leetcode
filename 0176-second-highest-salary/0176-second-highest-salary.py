import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    sorted_salary = employee['salary'].sort_values(ascending = False).drop_duplicates()
    if 2 > len(sorted_salary):
        return pd.DataFrame({f'SecondHighestSalary': [None]})
    else:
        nth_highest = sorted_salary.iloc[1]   
        return pd.DataFrame({f'SecondHighestSalary': [nth_highest]})
    