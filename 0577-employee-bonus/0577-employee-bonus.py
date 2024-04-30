import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    return employee.merge(bonus, how = "left").query("(bonus < 1000) | bonus.isna()")[["name","bonus"]]