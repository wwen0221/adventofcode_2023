import numpy as np
import re

def check_left(input_np,row,col):
    value = str(input_np[row,col-1])
    if value.isnumeric():
            return True
    else:
        return False


def check_right(input_np,row,col):
    value = str(input_np[row,col+1])
    if value.isnumeric():
            return True
    else:
        return False

def check_top(input_np,row,col):
    value = str(input_np[row-1,col])
    if value.isnumeric():
            return True
    else:
        return False

def check_bottom(input_np,row,col):
    value = str(input_np[row+1,col])
    if value.isnumeric():
            return True
    else:
        return False

def check_top_left(input_np,row,col):
    value = str(input_np[row-1,col-1])
    if value.isnumeric():
            return True
    else:
        return False

def check_top_right(input_np,row,col):
    value = str(input_np[row-1,col+1])
    # print('top right is: ', value)
    if value.isnumeric():
            return True
    else:
        return False

def check_bottom_left(input_np,row,col):
    value = str(input_np[row+1,col-1])
    # print('bottom left is: ', value)
    if value.isnumeric():
            return True
    else:
        return False

def check_bottom_right(input_np,row,col):
    value = str(input_np[row+1,col+1])
    # print('bottom right is: ', value)

    if value.isnumeric():
            return True
    else:
        return False

direction_dict = {0:'top_left',
                  1:'top',
                  2:'top_right',
                  3:'right',
                  4:'btm_right',
                  5:'btm',
                  6:'btm_left',
                  7:'left'}


def main():
    total = 0
    with open('input.txt') as f:
        input = f.readlines()

        input = [[*x.strip('\n')] for x in input]
        input_np = np.array(input)

        rows,cols = input_np.shape
        for row in range(rows):
            for col in range(cols):
                current_char = input_np[row,col]
                if current_char == '*':
                    current_list = []
                    
                    #check for all directions
                    top_left = check_top_left(input_np,row,col)
                    top = check_top(input_np,row,col)
                    top_right = check_top_right(input_np,row,col)
                    right = check_right(input_np,row,col)
                    btm_right = check_bottom_right(input_np,row,col)
                    btm = check_bottom(input_np,row,col)
                    btm_left = check_bottom_left(input_np,row,col)
                    left = check_left(input_np,row,col)
                    check_list = [top_left,top,top_right,right,btm_right,btm,btm_left,left]

                    engine_idx = [i for i, x in enumerate(check_list) if x == True]
                    directions = [direction_dict[i] for i in engine_idx]
                    processed_list = directions
                    

                    #print(processed_list)

                    #process 
                    if 'btm' in directions:
                        if 'btm_right' in directions:
                             processed_list.remove('btm_right')
                        if 'btm_left' in directions:
                             processed_list.remove('btm_left')

                    if 'top' in directions:
                        if 'top_right' in directions:
                             processed_list.remove('top_right')
                        if 'top_left' in directions:
                             processed_list.remove('top_left')
                             
                    if len(processed_list)>=2:

                        if 'top' in directions:
                            start_col = 0
                            end_col = 0
                            
                            current_row = row-1
                            curent_col = col
                            pointed_char = input_np[current_row,curent_col]
                            #get where it starts from
                            while pointed_char.isnumeric() and curent_col != 0:
                                 curent_col -=1
                                 start_col = curent_col
                                 pointed_char = input_np[current_row,curent_col]

                            temp_col = start_col+1
                            pointed_char = input_np[current_row,temp_col]
                            while pointed_char.isnumeric() and temp_col+1 != cols:
                                 temp_col+=1
                                 end_col = temp_col
                                 pointed_char = input_np[current_row,temp_col]

                            temp_list = input_np[current_row,start_col+1:end_col]
                            temp_list = ''.join(temp_list)
                            temp_list = temp_list.replace('.','')
                            current_list.append(temp_list)

                            directions.remove('top')
                            if 'top_left' in directions: directions.remove('top_left')
                            if 'top_right' in directions: directions.remove('top_right')

                        if 'btm' in directions:
                            start_col = 0
                            end_col = 0
                            
                            current_row = row+1
                            curent_col = col
                            pointed_char = input_np[current_row,curent_col]
         
                            while pointed_char.isnumeric() and curent_col != 0:
                                 curent_col -=1
                                 start_col = curent_col
                                 pointed_char = input_np[current_row,curent_col]

                            temp_col = start_col+1
                            pointed_char = input_np[current_row,temp_col]
                            while pointed_char.isnumeric() and temp_col+1 != cols:
                                 temp_col+=1
                                 end_col = temp_col
                                 pointed_char = input_np[current_row,temp_col]

                            temp_list = input_np[current_row,start_col+1:end_col]
                            temp_list = ''.join(temp_list)
                            temp_list = temp_list.replace('.','')
                            current_list.append(temp_list)

                            if 'btm_left' in directions: directions.remove('btm_left')
                            if 'btm_right' in directions: directions.remove('btm_right')

                        if 'left' in directions :
                            start_col = 0
                            end_col = col-1
                            curent_col = end_col
                            pointed_char = input_np[row,curent_col]
                            while pointed_char.isnumeric() and curent_col != 0:
                                curent_col-=1
                                start_col = curent_col
                                pointed_char = input_np[row,curent_col]

                            temp_list = input_np[row,start_col:end_col+1]
                            temp_list = ''.join(temp_list)
                            temp_list = temp_list.replace('.','')
                            current_list.append(temp_list)

                            if 'left' in check_list: check_list.remove('left')

                        if 'right' in directions:
                            start_col = col+1
                            end_col = 0
                            curent_col = start_col
                            pointed_char = input_np[row,curent_col]
                            while pointed_char.isnumeric() and curent_col+1 != cols:
                                curent_col+=1
                                end_col = curent_col
                                pointed_char = input_np[row,curent_col]

                            temp_list = input_np[row,start_col:end_col+1]
                            temp_list = ''.join(temp_list)
                            temp_list = temp_list.replace('.','')
                            current_list.append(temp_list)

                            directions.remove('right')

                        if len(directions)>0:
                             #check for diagonal
                             if 'top_left' in directions:
                                #print('top_left')
                                start_col = 0
                                end_col = col-1
                                
                                current_row = row-1
                                curent_col = col-1
                                pointed_char = input_np[current_row,curent_col]
 
                                while pointed_char.isnumeric() and curent_col != 0:
                                    curent_col -=1
                                    start_col = curent_col
                                    pointed_char = input_np[current_row,curent_col]

                                temp_col = start_col+1
                                pointed_char = input_np[current_row,temp_col]
                                while pointed_char.isnumeric() and temp_col+1 != cols:
                                    temp_col+=1
                                    end_col = temp_col
                                    pointed_char = input_np[current_row,temp_col]

                                temp_list = input_np[current_row,start_col:end_col]
                                temp_list = ''.join(temp_list)
                                temp_list = temp_list.replace('.','')
                                current_list.append(temp_list)
                        
                                if 'top_left' in directions: directions.remove('top_left')

                             if 'top_right' in directions:
             
                                start_col = col+1
                                end_col = 0
                                curent_col = start_col
                                pointed_char = input_np[row-1,curent_col]
                                while pointed_char.isnumeric() and curent_col+1 != cols:
                                    curent_col+=1
                                    end_col = curent_col
                                    pointed_char = input_np[row-1,curent_col]

                                temp_list = input_np[row-1,start_col:end_col+1]
                                temp_list = ''.join(temp_list)
                                temp_list = temp_list.replace('.','')
                                current_list.append(temp_list)

                                if 'top_right' in directions: directions.remove('top_right')
                            
                             if 'btm_right' in directions:
            
                                start_col = col+1
                                end_col = 0
                                curent_col = start_col
                                pointed_char = input_np[row+1,curent_col]
                                
                                while pointed_char.isnumeric() and curent_col+1 != cols:
                                    curent_col+=1
                                    end_col = curent_col
                                    pointed_char = input_np[row+1,curent_col]

                                temp_list = input_np[row+1,start_col:end_col+1]
                                temp_list = ''.join(temp_list)
                                temp_list = temp_list.replace('.','')
                                current_list.append(temp_list)

                                if 'btm_right' in directions: directions.remove('btm_right')
                            
                             if 'btm_left' in directions:
    
                                start_col = 0
                                end_col = col-1
                                
                                current_row = row+1
                                curent_col = col-1
                                pointed_char = input_np[current_row,curent_col]
                                #get where it starts from
                                while pointed_char.isnumeric() and curent_col != 0:
                                    curent_col -=1
                                    start_col = curent_col
                                    pointed_char = input_np[current_row,curent_col]

                                temp_col = start_col+1
                                pointed_char = input_np[current_row,temp_col]
                                while pointed_char.isnumeric() and temp_col+1 != cols:
                                    temp_col+=1
                                    end_col = temp_col
                                    pointed_char = input_np[current_row,temp_col]

                                temp_list = input_np[current_row,start_col:end_col]
                                temp_list = ''.join(temp_list)
                                temp_list = temp_list.replace('.','')
                                current_list.append(temp_list)
                        
                                if 'btm_left' in directions: directions.remove('btm_left')

                    if len(current_list)>0:
                        current_list = [int(i) for i in current_list]
                        total+= current_list[0]*current_list[1]

        print(total)


if __name__ == '__main__':
    main()