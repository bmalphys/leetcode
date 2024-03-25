import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    return (
        employee
        .rename(columns = {'name': 'Employee', 'salary': 'Salary'})
        .merge(
            department.rename(columns = {'id': 'departmentId', 'name': 'Department'}),
            on = 'departmentId', how ='inner')
        .merge(
            employee.rename(columns={'salary': 'Salary'}).loc[:, ['Salary', 'departmentId']]
            .drop_duplicates().groupby('departmentId')['Salary'].nlargest(3).reset_index(),
            on = ['Salary', 'departmentId'], how = 'inner')        
        .loc[:, ['Department', 'Employee', 'Salary']] )