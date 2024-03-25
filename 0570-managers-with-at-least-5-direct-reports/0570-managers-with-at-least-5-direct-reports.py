import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    result_df = employee.groupby('managerId')['id'].nunique().reset_index()
    manager_id_list = result_df[result_df['id'] >=5 ]['managerId'].values.tolist()
    return employee[employee['id'].isin(manager_id_list)][['name']]