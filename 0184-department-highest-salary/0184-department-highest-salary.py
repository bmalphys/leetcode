import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    merged = employee.merge(department, left_on = 'departmentId', right_on = 'id', suffixes = ('_employee', '_department'))
    highest_salary = merged.groupby('departmentId').apply(lambda x: x[x['salary'] == x['salary'].max()])
    highest_salary = highest_salary.reset_index(drop = True)
    result = highest_salary[['name_department', 'name_employee', 'salary']].rename(columns={'name_department':'Department', 'name_employee': 'Employee', 'salary': 'Salary'})
    return result

    result.columns = ['Department','Employee', 'Salary']

    return resul
    