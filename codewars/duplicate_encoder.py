'''
### kyu 6 ###
The goal of this exercise is to convert a string to a new string where each
character in the new string is "(" if that character appears only once in the
original string, or ")" if that character appears more than once in the original
string. Ignore capitalization when determining if a character is a duplicate.

Examples
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))((" 

Notes
Assertion messages may be unclear about what they display in some languages. If
you read "...It Should encode XXX", the "XXX" is the expected result, not the
input!
'''

def duplicate_encode(input_string:str) -> str:
    counting_dict = dict()
    out = []
    for c in input_string.lower():
        if c in counting_dict: counting_dict[c] += 1
        else: counting_dict[c] = 1
    for c in input_string.lower():
        if counting_dict[c] == 1:
            out.append('(')
        else:
            out.append(')')
    return ''.join(out)