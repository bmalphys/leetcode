import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    result_df = courses.groupby('class')['student'].nunique().reset_index() 
    return result_df[result_df['student'] >= 5][['class']]
    
    