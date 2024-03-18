import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:    
    accounts['category'] = accounts['income'].apply(lambda x: 'Low Salary' if x < 20000 else 'Average Salary' if x>= 20000 and x <= 50000  else 'High Salary')
    account_df = pd.DataFrame({'category': pd.Categorical(accounts['category'],  categories = ['Low Salary' , 'Average Salary', 'High Salary'])})
    return account_df['category'].value_counts().reset_index().rename(columns = {'count': 'accounts_count'})