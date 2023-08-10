'''
Write a method that takes a field for well-known board game "Battleship" as an
argument and returns true if it has a valid disposition of ships, false
otherwise. Argument is guaranteed to be 10*10 two-dimension array. Elements in
the array are numbers, 0 if the cell is free and 1 if occupied by ship.

Battleship (also Battleships or Sea Battle) is a guessing game for two players.
Each player has a 10x10 grid containing several "ships" and objective is to
destroy enemy's forces by targetting individual cells on his field. The ship
occupies one or more cells in the grid. Size and number of ships may differ from
version to version. In this kata we will use Soviet/Russian version of the game.

Before the game begins, players set up the board and place the ships accordingly
to the following rules: There must be single battleship (size of 4 cells), 2
cruisers (size 3), 3 destroyers (size 2) and 4 submarines (size 1). Any
additional ships are not allowed, as well as missing ships. Each ship must be a
straight line, except for submarines, which are just single cell.

The ship cannot overlap or be in contact with any other ship, neither by edge
nor by corner.
'''


class Game():
    def __init__(self) -> None:
        self.ships = {
            4: 1,  # One battleship of size 4
            3: 2,  # Two cruisers of size 3 each
            2: 3,  # Three destroyers of size 2 each
            1: 4   # Four submarines of size 1 each
        }

    def valid_ship(self,length:int)->bool:
        if(length in self.ships):
            if(self.ships[length]>0):
                return True
        return False

    def deduct_ship(self,length:int)->None:
        self.ships[length]-=1

def is_ocean(i:int,j:int,direction:int,count:int,field)->bool:
    if(direction==1): #vertical
        if(len(field)-1!=j): #not last row
            if(i!=0):

                if(field[i-1][j+1]==1):
                    return False
            if(i!=len(field)-1):
                if(field[i+1][j+1]==1):
                    return False

    else: #horizontal
        pass


def validate_battlefield(field):
    game=Game()
    for i in range(len(field)):
        count_length=0
        for j in range(len(field)):
            if(field[i][j]==1):
                count_length+=1
            else:
                if(count_length):
                    if(game.valid_ship(count_length)):
                        #check the surrounding waters

                        game.deduct_ship(count_length)
                    else:
                        return False
    return True