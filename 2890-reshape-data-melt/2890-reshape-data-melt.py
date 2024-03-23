import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    result_df = pd.melt(report, id_vars = ['product'], 
            value_vars = ['quarter_1', 'quarter_2', 'quarter_3', 'quarter_4'])
    return result_df.rename(columns = {'variable': 'quarter', 'value': 'sales' })
    