import pandas as pd


def read_txt(txt_path):
    df = pd.read_table(txt_path, delimiter=':',header=None)
    df.columns = ["cards","full_results"]
    return df


if __name__ == '__main__':
    df = read_txt('input.txt')
    df[['winner_lst','results']] = df.full_results.str.split("|",expand=True) 
    total_points = 0

    for idx,rows in df.iterrows():
        total = 0
        winner_lst = rows['winner_lst'].strip().split(' ')
        results = rows['results'].strip().split(' ')
        results = [x for x in results if x != ""]
    
        won = list(set(results).intersection(winner_lst))
        result = 0
        if len(won) >=1:
            if len(won) == 1:
                result = 1
            else:
                for idx, ele in enumerate(won):
                    if idx ==0:
                        result = 1
                    else:
                        result *=2
        
        total_points += result
    
    print(total_points)
