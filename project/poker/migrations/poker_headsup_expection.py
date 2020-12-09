import numpy as np
from poker_headsup_deck import make_list_num
from poker_headsup_deck import make_list_mark

# player is "number" list (size:2), comunitee (size:0/3/4/5)

def auts_main(player, comunitee):
    aut = 0
    player_num = make_list_num(player, 2)
    #player_mark = make_list_mark(player, 2)
    comunitee_num = make_list_num(comunitee, len(comunitee))
    #comunitee_mark = make_list_mark(comunitee, len(comunitee))

    aut += auts_num(player_num, comunitee_num)
    aut += auts_straight(player_num, comunitee_num)
    return aut

def auts_num(player, comunitee): 
    a = 0
    if player[0] != player[1]:
        a += 6
    elif player[0] == player[1]:
        a += 2
    for i in comunitee:
        if i in player:
            a -= 1

    return a

def auts_straight(player, comunitee):
    b = 0
    player += comunitee
    player.sort()
    s_player = min(set(player))
    s_player -= 1
    r = len(set(player))
    if 5<=r and r<=7:
        i = 0
        while i == 13:
            s_player += 1
            if s_player+1 in s_player and s_player+2 in s_player and s_player+3 in s_player and s_player+4 in s_player:
                b = 0
            i += 1
    elif 4<=r and r<=6:
        for i in range(r-4):
            if s_player+1 in s_player and s_player+2 in s_player and s_player+3 in s_player:
                b += 8
            elif s_player+2 in s_player and s_player+3 in s_player and s_player+4 in s_player:
                b += 4
            elif s_player+1 in s_player and s_player+3 in s_player and s_player+4 in s_player:
                b += 4
            elif s_player+1 in s_player and s_player+2 in s_player and s_player+4 in s_player:
                b += 4
    else:
        b = 0
    return b



