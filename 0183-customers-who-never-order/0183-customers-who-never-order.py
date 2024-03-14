import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame(customers[~customers['id'].isin(orders['customerId'].values)]['name'])
    return df.rename(columns = {'name': 'Customers'})
    