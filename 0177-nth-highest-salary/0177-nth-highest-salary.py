import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    sorted_salary = employee['salary'].sort_values(ascending = False).drop_duplicates()
    if N > len(sorted_salary) or N <= 0:
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    else:
        nth_highest = sorted_salary.iloc[N-1]   
        return pd.DataFrame({f'getNthHighestSalary({N})': [nth_highest]})