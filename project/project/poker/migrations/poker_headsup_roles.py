import numpy as np

def roles(number, suit):
    flag = [False, False]
    number.sort()

    # suit 
    mark_duplicate = 0
    for i in set(suit):
        if mark_duplicate < suit.count(i):
            mark_duplicate = suit.count(i)
    if mark_duplicate >= 5:
        flag[0] = True

    # number
    num_duplicate = 0
    for i in set(number):
        if num_duplicate < number.count(i):
            num_duplicate = number.count(i)

    # straight
    for i in range(3):
        min_num = number[i]
        if min_num+1 in number and min_num+2 in number and min_num+3 in number and min_num+4 in number:
            flag[1] = True
            break
    if 1 in number and 10 in number and 11 in number and 12 in number and 13 in number:
        flag[1] = True


    score = 0
    # straight flusf
    if flag[0] and flag[1]:
        score = 8
    # four card
    elif len(set(number)) == 4 and num_duplicate == 4:
        if num_duplicate == 4:
            score = 7
    elif len(set(number)) == 3 and num_duplicate == 4:
        score = 7
    elif len(set(number)) == 2 and num_duplicate == 4:
        score = 7
    # full house
    elif len(set(number)) == 4 and num_duplicate == 3:
        score = 6
    elif len(set(number)) == 3 and num_duplicate == 3:
        score = 6
    # flush
    elif flag[0]:
        score = 5
    # straight
    elif flag[1]:
        score = 4
    # three card
    elif len(set(number)) == 5 and num_duplicate == 3:
        score = 3
    # two pair
    elif len(set(number)) == 5 or len(set(number)) == 4:
        if num_duplicate == 2:
            score = 2
    # one pair
    elif len(set(number)) == 6 and num_duplicate == 2:
        score = 1
    
    return score

def roles_name(i):
    if 8<=i and i<9:
        return 'straight flush'
    elif 7<=i and i<8:
        return 'four card'
    elif 6<=i and i<7:
        return 'fullhouse'
    elif 5<=i and i<6:
        return 'flush'
    elif 4<=i and i<5:
        return 'straight'
    elif 3<=i and i<4:
        return 'three card'
    elif 2<=i and i<3:
        return 'two pair'
    elif 1<=i and i<2:
        return 'one pair'
    elif 0<=i and i<1:
        return 'high card'