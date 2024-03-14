import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df1 = pd.DataFrame()
    df1['id'] = views[views['author_id'] == views['viewer_id']][['author_id']]
    return df1.drop_duplicates().sort_values(by = ['id'])
    