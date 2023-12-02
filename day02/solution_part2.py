import pandas as pd
import re


def read_txt(txt_path):
    df = pd.read_table(txt_path, delimiter=':',header=None)
    df.columns = ["game","results"]
    return df

def process(x):
    
    limit = {'red cubes': 12, 
             'green cubes': 13 , 
             'blue cubes': 14
    } 
       
    return_dict = {
        'red' : [],
        'blue' : [],
        'green' : []
    }

    drawings = x['results'].split(';')
    for each_draw in drawings:
        color = each_draw.split(',')
        for each_color in color:
                count = re.sub("[^0-9]", "", each_color)
                color = re.findall(r"(?=(green|red|blue))", each_color)[0]
                return_dict[color].append(int(count))
    
    x['maximum'] = max(return_dict['red'])*(max(return_dict['blue'])*(max(return_dict['green'])))

    return x
        


if __name__ == '__main__':
    df = read_txt('input.txt')
    df['game_idx'] = df['game'].apply(lambda x: x.strip("Game "))
    df = df.apply(process, axis=1)
    print(df)
    total = df['maximum'].sum()
    print(total)