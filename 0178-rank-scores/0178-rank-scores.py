import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    df = scores[['score']].sort_values(by = 'score', ascending = False)
    df['rank'] = df.rank(method = 'dense', ascending = False)
    return df
    