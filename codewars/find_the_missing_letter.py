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

    def __init__(self, letters:list[str]) -> None:
        self.letters = letters

    def get_missing_letter(self) -> str:
        last_index = None
        for letter in self.letters:
            current_index = Missing.alphabet_dict[letter.upper()]
            if last_index is not None and current_index - last_index != 1:
                return self.match_index(current_index - 1, letter)
            else:
                last_index = current_index

    def match_index(self, target_index, letter:str) -> str:
        for k,v in Missing.alphabet_dict.items():
            if v == target_index:
                if letter.isupper():
                    return k
                else:
                    return k.lower()

def find_missing_letter(chars:list[str]) -> str:
    missing =  Missing(chars)
    return missing.get_missing_letter()

tests =[['a','b','c','d','f'], ['O','Q','R','S'], ['b','d'], ['a', 'c', 'd']]
for test in tests:
    print(find_missing_letter(test))