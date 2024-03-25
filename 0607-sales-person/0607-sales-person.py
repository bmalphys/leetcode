import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    com_list = company[company['name'] == 'RED']['com_id'].values.tolist()
    order_list = orders[orders['com_id'].isin(com_list)]['sales_id'].values.tolist()
    return sales_person[~sales_person['sales_id'].isin(order_list)][['name']]