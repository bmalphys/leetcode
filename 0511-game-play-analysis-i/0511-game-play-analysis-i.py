import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    result_df = activity.groupby('player_id')['event_date'].min().reset_index()
    return result_df.rename(columns = {'event_date': 'first_login'})

    