import numpy as np

from django import forms
from django.shortcuts import render
from django.http import HttpResponse

from poker_headsup_deck import card_deck
from poker_headsup_deck import draw
from poker_headsup_deck import make_list_num
from poker_headsup_deck import make_list_mark
from poker_headsup_deck import check
from poker_headsup_roles import roles
from poker_headsup_roles import roles_name
#from poker_headsup_action import Action

#heads up (player and robot)
number_players = 2

# position (True : player, False : robot) 
BB_posi = True
SB_posi = False
flag = SB_posi
checker = [False, False]

# blind
BB = 100
SB = 50
pot = BB + SB
luck = SB
bets = 0
# stuck
stuck_player = 50 * BB
stuck_robot = 50 * BB

class Action:
    def __init__(self, pot, stuck_player, stuck_robot ,flag):
        self.pot = pot
        self.stuck_player = stuck_player
        self.stuck_robot = stuck_robot
        self.flag = flag

    # newgame

    def newgame_a(self):
        self.pot = BB + SB
        if(flag):
            print("BB is robot : " + str(BB) + " / SB is player : " + str(SB))
            self.stuck_player -= SB
            self.stuck_robot -= BB
        else:
            print("BB is player : " + str(BB) + " / SB is robot : " + str(SB))
            self.stuck_robot -= SB
            self.stuck_player -= BB

    # situation

    def situation_a(self):
        print("Pot:" + str(self.pot) + "/Player's stuck:" + str(self.stuck_player) + "/Robot's stuck:" + str(self.stuck_robot))
        print()

    # action: check

    def check_a(self):
        print()
        print("The last player's action was check")
        print()

    # action: call

    def call_a(self, luck):
        self.luck = luck
        #self.stuck_player = stuck_player
        #self.stuck_robot = stuck_robot
        self.pot += self.luck
        if(flag):
            self.stuck_player -= self.luck
        else:
            self.stuck_robot -= self.luck
        print()
        print("The last player's action was call")
        print()

    # action: raise

    def raise_a(self, bets):
        self.bets = bets
        #self.stuck_player = stuck_player
        #self.stuck_robot = stuck_robot
        self.pot += self.bets
        if(flag):
            self.stuck_player -= self.bets
        else:
            self.stuck_robot -= self.bets
        print()
        print("The last player's action was " + str(self.bets) + "bet")
        print()
                
    # action: fold

    def fold_a(self):
        print()
        print("The last player's action was fold")
        print()
        if(flag):
            print("The robot is winner !" )
            self.stuck_robot += self.pot
        else:
            print("The player is winner !" )
            self.stuck_player += self.pot
        self.pot = BB + SB
        print()
        print()
        print("Next Game")
        print()
        print()
    
    def win_a(self, bol):
        if(bol):
            self.stuck_player += self.pot
        else:
            self.stuck_robot += self.pot
        self.pot = BB + SB
        print()
        print()
        print("Next Game")
        print()
        print()

# ====================================================-

        
action = Action(pot, stuck_player, stuck_robot,flag)
stuck_player += SB
stuck_robot += BB

# -------------------------------------------------------------------------------------------------

while stuck_player != 0 or stuck_robot != 0:

    if(BB_posi):
        BB_posi = False
        SB_posi = True
    else:
        BB_posi = True
        SB_posi = False

    flag = SB_posi
    luck = SB

    # preflop - flop - turn - river

    action.newgame_a()
    now_step = 0
    checker = [False, False]
           
    # preflop
    while 0 <= now_step and now_step <= 4:

        if(checker[0] and checker[1]):
            flag = BB_posi
            now_step += 1
            bets = 0
            luck = 0
            checker = [False, False]
            continue

        if(now_step == 0):
            print("preflop")
            comunitee_card = draw(card_deck(), 5)
            bol = True
            while(bol):
                player_card = draw(card_deck(), 2)
                bol = check(comunitee_card, player_card)
            boo = [True, True]
            while(boo[0] and boo[1]):
                robot_card = draw(card_deck(), 2)
                boo[0] = check(comunitee_card, robot_card)
                boo[1] = check(player_card, robot_card)
            print(player_card)
            print(robot_card)

        elif(now_step == 1):
            print("flop")
            print(player_card)
            print(robot_card)
            print(comunitee_card[:3])

        elif(now_step == 2):
            print("turn")
            print(player_card)
            print(robot_card)
            print(comunitee_card[:4])

        elif(now_step == 3):
            print("river")
            print(player_card)
            print(robot_card)
            print(comunitee_card)

        elif now_step == 4:
            print("showdown")
            player_card += comunitee_card
            robot_card += comunitee_card

            player_card_num = make_list_num(player_card, 7)
            player_card_mark = make_list_mark(player_card, 7)
            player_result = roles(player_card_num, player_card_mark)
            player_roles = roles_name(player_result)

            robot_card_num = make_list_num(robot_card, 7)
            robot_card_mark = make_list_mark(robot_card, 7)
            robot_result = roles(robot_card_num, robot_card_mark)
            robot_roles = roles_name(robot_result)

            print("Player is " + player_roles + ".")
            print("Robot is " + robot_roles + ".")
            if player_result > robot_result:
                print("Player is winner!")
                action.win_a(True)
            else:
                print("Robot is winner!")
                action.win_a(False)
            now_step = 0

        action.situation_a()
        # preflop: action is player
        if(flag):
            print("Player's action.")
            act = str(input())

            if(act == "call"):
                checker[0] = True
                action.call_a(luck)
                flag = False
                continue

            elif(act == "check"):
                action.check_a()
                checker[0] = True
                flag = False
                continue

            elif(act == "raise"):
                checker = [True, False]
                print("How much ?")
                bets = int(input())
                action.raise_a(bets)
                flag = False
                continue

            elif(act == "fold"):
                action.fold_a()
                now_step = 0
                break

            else:
                print("Please follow the sentence.")
                continue
        
        # preflop: action is robot
        else:
            print("Robot's action.")
            #act = input()
            if checker[0] == True and checker[1] == False:
                act = "call"
            else:
                act = "check"

            if(act == "call"):
                checker[1] = True
                action.call_a(luck)
                continue

            if(act == "check"):
                action.check_a()
                checker[1] = True
                flag = True
                continue

            elif(act == "raise"):
                checker = [False, True]
                print("How much ?")
                bets = int(input())
                action.raise_a(bets)
                flag = True
                continue

            elif(act == "fold"):
                action.fold_a()
                now_step = 0
                break
        
    # showdown

    if(now_step == 4):
        print()
        print("ゲーム終了")
        print()
# ------------------------------------------------------------------------------

if stuck_player == 0:
    print("The player won all the stucks.")
elif stuck_robot == 0:
    print("The robot won all the stucks.")