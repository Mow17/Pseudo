import numpy as np
from poker_headsup_roles import roles
from poker_headsup_roles import roles_name
#from poker_headsup_expection import auts_main

MARK = "♤", "♧", "♡", "♢"
NUMBER = [1,2,3,4,5,6,7,8,9,10,11,12,13]
NUMBER_4 = [1,2,3,4,5,6,7,8,9,10,11,12,13]*4

action_0 = "call"
action_1 = "check"
action_2 = "raise"
action_3 = "fold"

def card_deck():
    deck_list = [f'{mark}{number}'
                 for mark in MARK
                 for number in NUMBER]

    #deck_master = dict(zip(deck_list, NUMBER_4))
    np.random.shuffle(deck_list)

    return deck_list


def draw(deck_list, n):
    player_card = deck_list[:n]
    del deck_list[:n]

    return player_card

def make_list_num(lists, n):
    list_num = []
    for i in range(n):
        card = lists[i]
        number = card[1:]
        list_num.append(int(number))
    return list_num

def make_list_mark(lists, n):
    list_mark = []
    for i in range(n):
        card = lists[i]
        mark = card[0]
        list_mark.append(str(mark))
    return list_mark

def check(comunitee, player):
    for i in range(2):
        if player[i] in comunitee:
            return True
    return False

deck = card_deck()

player_card = draw(deck,2)
comunitee_card = draw(deck, 5)
#player_card += comunitee_card

player_card_num = make_list_num(player_card, 2)
player_card_mark = make_list_mark(player_card, 2)
#player_result = roles(player_card_num, player_card_mark)
comunitee_card_num = make_list_num(comunitee_card, 5)
comunitee_card_mark = make_list_mark(comunitee_card, 5)

#print(player_card)
#print(comunitee_card[:3])
#print(player_result)
#print(roles_name(player_result))

#ans = auts_main(player_card, comunitee_card)
#print(ans)

