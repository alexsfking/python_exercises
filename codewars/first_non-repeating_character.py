'''
### kyu 5 ###
Write a function named first_non_repeating_letter that takes a string input, and
returns the first character that is not repeated anywhere in the string.

For example, if given the input 'stress', the function should return 't', since
the letter t only occurs once in the string, and occurs first in the string.

As an added challenge, upper- and lowercase letters are considered the same
character, but the function should return the correct case for the initial
letter. For example, the input 'sTreSS' should return 'T'.

If a string contains all repeating characters, it should return an empty string
("") or None -- see sample tests.
'''

def first_non_repeating_letter(string:str)->str:
    character_dict=dict()
    for c in string:
        if c.islower():
            if c in character_dict:
                character_dict[c] += 1
            else:
                if c.upper() in character_dict:
                    character_dict[c.upper()] += 1
                else:
                    character_dict[c] = 1
        else:
            if c in character_dict:
                character_dict[c] += 1
            else:
                if c.lower() in character_dict:
                    character_dict[c.lower()] += 1
                else:
                    character_dict[c] = 1
    for k, v in character_dict.items():
        if v == 1:
            return k
    return ""