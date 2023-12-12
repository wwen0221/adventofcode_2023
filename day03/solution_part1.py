import numpy as np
import re

def check_left(input_np,row,col):
    value = str(input_np[row,col-1])
    if not value.isnumeric():
        if value!='.':
            return True
        else:
            return False
    return False


def check_right(input_np,row,col):
    value = str(input_np[row,col+1])

    if not value.isnumeric():
        if value!='.':
            return True
        else:
            return False
    return False

def check_top(input_np,row,col):
    value = str(input_np[row-1,col])

    if not value.isnumeric():
        if value!='.':
            return True
        else:
            return False
    return False

def check_bottom(input_np,row,col):
    value = str(input_np[row+1,col])
    #print('bottom is: ', value)
    if not value.isnumeric():
        if value!='.':
            return True
        else:
            return False
    return False

def check_top_left(input_np,row,col):
    value = str(input_np[row-1,col-1])

    if not value.isnumeric():
        if value!='.':
            return True
        else:
            return False
    return False

def check_top_right(input_np,row,col):
    value = str(input_np[row-1,col+1])
    #print('top right is: ', value)
    if not value.isnumeric():
        if value!='.':
            return True
        else:
            return False
    return False

def check_bottom_left(input_np,row,col):
    value = str(input_np[row+1,col-1])

    if not value.isnumeric():
        if value!='.':
            return True
        else:
            return False
    return False

def check_bottom_right(input_np,row,col):
    value = str(input_np[row+1,col+1])

    if not value.isnumeric():
        if value!='.':
            return True
        else:
            return False
    return False


def main():
    total = 0
    with open('input.txt') as f:
        input = f.readlines()

        input = [[*x.strip('\n')] for x in input]
        input_np = np.array(input)

        rows,cols = input_np.shape
        for row in range(rows):
            has_adjescent = False
            char_lst = ''
            for col in range(cols):
                current_char = input_np[row,col]
                
                try:
                    char = int(current_char)
                    char_lst+=current_char

                    #check adjacent 
                    if row == 0:
                        if col==0:
                            #check for right, bottom right, bottom
                            right = check_right(input_np,row,col)
                            btm_right = check_bottom_right(input_np,row,col)
                            btm = check_bottom(input_np,row,col)

                            if right == True or btm_right == True or btm == True:
                                has_adjescent = True
                            
                        elif col == cols:
                            #check for left, bottom, bottom left
                            left = check_left(input_np,row,col)
                            btm = check_bottom(input_np,row,col)
                            btm_left = check_bottom_left(input_np,row,col)

                            if left == True or btm == True or btm_left == True:
                                has_adjescent = True

                        else:
                            #check for left,bottom left, bottom, bottom right, right
                            right = check_right(input_np,row,col)
                            btm_right = check_bottom_right(input_np,row,col)
                            btm = check_bottom(input_np,row,col)
                            btm_left = check_bottom_left(input_np,row,col)
                            left = check_left(input_np,row,col)

                            if right == True or btm_right == True or btm == True or btm_left == True or left == True:
                                has_adjescent = True

                    elif row == rows-1:
                        if col == 0:
                            #check for top, top right, right
                            top = check_top(input_np,row,col)
                            top_right = check_top_right(input_np,row,col)
                            right = check_right(input_np,row,col)

                            if top == True or top_right == True or right == True:
                                has_adjescent = True

                        elif col == cols-1:
                            #check for top, top left, left
                            top_left = check_top_left(input_np,row,col)
                            top = check_top(input_np,row,col)
                            left = check_left(input_np,row,col)
                            if top_left == True or top == True or left == True:
                                has_adjescent = True

                        else:
                            #check for left, top left, top, top right, right 
                            top_left = check_top_left(input_np,row,col)
                            top = check_top(input_np,row,col)
                            top_right = check_top_right(input_np,row,col)
                            right = check_right(input_np,row,col)
                            left = check_left(input_np,row,col)
                            if top_left == True or top == True or top_right == True or right == True or left == True:
                                has_adjescent = True

                    else:
                            #check for all directions
                            top_left = check_top_left(input_np,row,col)
                            top = check_top(input_np,row,col)
                            top_right = check_top_right(input_np,row,col)
                            right = check_right(input_np,row,col)
                            btm_right = check_bottom_right(input_np,row,col)
                            btm = check_bottom(input_np,row,col)
                            btm_left = check_bottom_left(input_np,row,col)
                            left = check_left(input_np,row,col)

                            if top_left == True or top == True or top_right == True or right == True or btm_right == True \
                            or btm == True or btm_left == True or left == True:
                                has_adjescent = True

                except:
                    if has_adjescent == True:
                        total+= int(char_lst)
                    char_lst = ''
                    has_adjescent = False

        print(total)


if __name__ == '__main__':
    main()