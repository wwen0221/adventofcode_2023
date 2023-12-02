import pandas as pd
import re

def read_txt(txt_path):
    df = pd.read_table(txt_path, delimiter=' ',header=None)
    df.columns = ["data"]
    return df

def get_first_last_digit(x):
    digit_lst = ['1','2','3','4','5','6','7','8','9']
    str_to_digit_dict = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }
    if len(x)>=2:
        first = x[0]
        last = x[-1]
        if first not in digit_lst:
            first = str_to_digit_dict[first]
        if last not in digit_lst:
            last = str_to_digit_dict[last] 

        x = first+last
    elif len(x) == 1:
        x = x[0]
        x = x+x
    return x

if __name__ == "__main__":
    df = read_txt('input.txt')
    string_lst = ['one', 'two', 'three', 'four','five','six','seven','eight','nine','1','2','3','4','5','6','7','8','9']

    #df['cleaned_up'] = df['data'].apply(lambda x: re.sub("[^0-9]", "", x))
    df['cleaned_up'] = df['data'].apply(lambda x: re.findall(r"(?=("+'|'.join(string_lst)+r"))", x))
    df['final_ans'] = df['cleaned_up'].apply(lambda x: get_first_last_digit(x))
    print(df)
    df['final_ans'] = pd.to_numeric(df['final_ans'])
    sum = df['final_ans'].sum()
    print(sum)
