import pandas as pd
import re

def read_txt(txt_path):
    df = pd.read_table(txt_path, delimiter=' ',header=None)
    df.columns = ["data"]
    return df

def get_first_last_digit(x):
    if len(x)>2:
        first = x[0]
        last = x[-1]
        x = first+last
    elif len(x) == 1:
        x = x+x
    return x

if __name__ == "__main__":
    df = read_txt('input.txt')
    df['cleaned_up'] = df['data'].apply(lambda x: re.sub("[^0-9]", "", x))
    df['final_ans'] = df['cleaned_up'].apply(lambda x: get_first_last_digit(x))
    df['final_ans'] = pd.to_numeric(df['final_ans'])
    sum = df['final_ans'].sum()

