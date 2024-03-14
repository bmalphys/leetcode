import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
        allowed_chars = set("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-.")
        users['mail'] = users['mail'].apply(lambda x: 'wrong' if 
                                        (x.rsplit("@", 1)[-1] != "leetcode.com" or
                                         set(x.rsplit("@", 1)[0]).issubset(allowed_chars) == False or
                                         x.rsplit("@", 1)[0][0].isalpha() == False) else x)
        users = users.drop(users[users['mail'] == 'wrong'].index)
        return users
    