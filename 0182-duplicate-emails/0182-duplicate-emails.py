import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame(person.loc[person.duplicated(subset=['email']), ['email']]).drop_duplicates()
    
    