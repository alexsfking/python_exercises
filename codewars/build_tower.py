'''
### kyu 6 ###
Build Tower
Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. A tower block is represented with "*" character.

For example, a tower with 3 floors looks like this:

[
  "  *  ",
  " *** ", 
  "*****"
]
And a tower with 6 floors looks like this:

[
  "     *     ", 
  "    ***    ", 
  "   *****   ", 
  "  *******  ", 
  " ********* ", 
  "***********"
]
'''

def tower_builder(n_floors:int)->list:
    out=[]
    length=(n_floors-1)*2+1
    for i in range(n_floors):
        asterisks=i*2+1
        spaces=(length-asterisks)//2
        out.append(spaces*' '+asterisks*'*'+spaces*' ')
    return out
