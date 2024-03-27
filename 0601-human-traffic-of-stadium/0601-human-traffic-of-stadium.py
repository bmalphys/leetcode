import pandas as pd

def human_traffic(stadium: pd.DataFrame) -> pd.DataFrame:
    df = stadium.sort_values("id").query("people>=100").reset_index(drop = 1)
    return df.loc[df.groupby(df['id'] - df.index)["id"].transform("count")>=3]    