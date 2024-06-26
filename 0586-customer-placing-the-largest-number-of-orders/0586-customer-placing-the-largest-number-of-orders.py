import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    result_df = orders.groupby('customer_number')['order_number'].nunique().reset_index()
    return result_df[result_df['order_number'] == result_df['order_number'].max()][['customer_number']]
    