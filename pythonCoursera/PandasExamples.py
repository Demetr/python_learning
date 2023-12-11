# Dataframes from Dictionaries Usind Pandasa with examples
import pandas as pd


def dict_data_frame():
    dictionary = {'p': [1, 3, 2, 6, 3, 7, 8, 9], 'q': [4, 3, 2, 3, 2, 6, 9, 8], 'r': [4, 0, 9, 4, 3, 2, 3, 2]}
    print(dictionary)
    df = pd.DataFrame(dictionary)
    print(df)
    # new_df = df.iloc[2:5, 'q']
    # print(new_df)
    new_df0 = df.loc[2:5, 'q']
    print(new_df0)
    new_df1 = df.iloc[2:6, 1]
    print(new_df1)
    # new_df2 = df.loc[2:5, 1]
    # print(new_df2)
