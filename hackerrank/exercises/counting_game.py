#!/bin/python3

import math
import os
import random
import re
import sys

"""
Louise and Richard have developed a numbers game. They pick a number and check to see if it is a power
of 2. If it is, they divide it by 2. If not, they reduce it by the next lower number which is a power 
of 2. Whoever reduces the number to 1 wins the game. Louise always starts.

Given an initial value, determine who wins the game.

Example:
n=132
It's Louise's turn first. She determines that 132 is not a power of 2. The next lower power of 2 is 128,
so she subtracts that from 132 and passes 4 to Richard. 4 is a power of 2, so Richard divides it by 2 
and passes 2 to Louise. Likewise, 2 is a power so she divides it by 2 and reaches 1. She wins the game.
"""

#
# Complete the 'counterGame' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#

class Player(object):
    def __init__(self, name):
        self.name=name
        
    def get_name(self):
        return(self.name)
        

class Game(object):
    def __init__(self, *players:str):
        self.players=[]
        self.turn=0
        for player in players:
            self.players.append(Player(player))
        self.create_table()
            
    def whose_turn_is_it(self):
        if(self.turn<len(self.players)):
            pass
        else:
            self.turn=0
        return(self.turn)
    
    def increment_player_turn(self):
        self.turn=self.turn+1
        
    def is_legal_move(self,n):
        if(n>1):
            return True
        else:
            return False
        
    def create_table(self):
        self.d=dict()
        for i in range(1,64):
            self.d[pow(2,i)]=pow(2,i)
            
    def make_move(self, n):
        if(n in self.d):
            return(n//2)
        for k in self.d.keys():
            if(k>n):
                return(n-(k//2))
        raise Exception("Outside scope")
        
    def begin(self,n):
        gameover=False
        move=n
        while gameover is False:
            if(self.is_legal_move(move)):
                move=self.make_move(move)
                self.whose_turn_is_it()
                if(move==1):
                    return(self.players[self.whose_turn_is_it()].get_name())
                self.increment_player_turn()
            else:
                self.whose_turn_is_it()
                self.increment_player_turn()
                return(self.players[self.whose_turn_is_it()].get_name())
                
                
                
def counterGame(n):
    game=Game('Louise','Richard')
    result=game.begin(n)
    return(result)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = counterGame(n)

        fptr.write(result + '\n')

    fptr.close()
