'''
### kyu 6 ###
Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a
= 1, b = 2, c = 3 etc.

For example, the score of abad is 8 (1 + 2 + 1 + 4).

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the
original string.

All letters will be lowercase and all inputs will be valid.
'''

alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower())
scoring_dict = {letter: index + 1 for index, letter in enumerate(alphabet)}

def high(input_string:str) -> str:
    word_score_dict = {}
    words = input_string.split()
    for word in words:
        word_score_dict[word] = 0
        for char in word:
            if char in scoring_dict:
                word_score_dict[word] += scoring_dict[char]
    highest = max(word_score_dict.values())
    for k, v in word_score_dict.items():
        if v == highest:
            return k

print(high('man i need a taxi up to ubud') == 'taxi')