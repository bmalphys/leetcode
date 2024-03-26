import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(person, address, on = 'personId', how = 'outer').drop(['addressId', 'personId'], axis = 1)
    df.dropna(subset=['lastName', 'firstName'], inplace=True)
    return df
    