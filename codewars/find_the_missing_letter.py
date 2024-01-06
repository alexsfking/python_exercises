'''
### kyu 6 ###
Write a method that takes an array of consecutive (increasing) letters as input
and that returns the missing letter in the array.

You will always get an valid array. And it will be always exactly one letter be
missing. The length of the array will always be at least 2.
The array will always contain letters in only one case.

Example:

['a','b','c','d','f'] -> 'e'
['O','Q','R','S'] -> 'P'
(Use the English alphabet with 26 letters!)
'''

class Missing:
    alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    alphabet_dict = {letter: index for index, letter in enumerate(alphabet)}

    def __init__(self, letters:list) -> None:
        for letter in letters:
            

    def missing(self):
        pass

def find_missing_letter(chars:list[str]) -> str:
    