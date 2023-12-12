import pandas as pd


card_dict = {}

def read_txt(txt_path):
    df = pd.read_table(txt_path, delimiter=':',header=None)
    df.columns = ["cards","full_results"]
    return df


if __name__ == '__main__':
    df = read_txt('input.txt')
    df['card_idx'] = df['cards'].apply(lambda x: x.split('Card ')[-1])
    df[['winner_lst','results']] = df.full_results.str.split("|",expand=True) 
    total_points = 0

    for idx,rows in df.iterrows():
        total = 0
        copy_no = 0
        current_card = rows['card_idx'].strip()
        print(f'current card: {current_card}')

        winner_lst = rows['winner_lst'].strip().split(' ')
        results = rows['results'].strip().split(' ')
        results = [x for x in results if x != ""]
    
        won = list(set(results).intersection(winner_lst))
        #check if the current card has record 
        if current_card in card_dict.keys():
            copy_no = card_dict[current_card]

        if current_card not in card_dict.keys():
            card_dict[current_card] = 1
        else:
            card_dict[current_card]+=1

        for n in range(1,len(won)+1):
            if str(int(current_card)+n) not in card_dict.keys():
                card_dict[str(int(current_card)+n)] = 1 + copy_no
            else:
                card_dict[str(int(current_card)+n)]+= copy_no + 1
    
        
    for key,val in card_dict.items():
        total_points+= val

    print(total_points)
