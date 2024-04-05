import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather.sort_values(by = ['recordDate'], inplace = True)
    return weather.loc[weather['temperature'] - weather['temperature'].shift(1) > 0][['id']] 
    