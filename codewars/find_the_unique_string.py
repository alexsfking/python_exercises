'''
### kyu 5 ###
There is an array of strings. All strings contains similar letters except one. Try to find it!

find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]) # => 'BbBb'
find_uniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]) # => 'foo'
Strings may contain spaces. Spaces are not significant, only non-spaces symbols matters. E.g. string that contains only spaces is like empty string.

It’s guaranteed that array contains more than 2 strings.

This is the second kata in series:

Find the unique number
Find the unique string (this kata)
Find The Unique
'''

def find_uniq(array:list[str]) -> str:
    letter_counter_dict=dict()
    for s in array:
        for c in list(set(s.lower())):
            if c in letter_counter_dict:
                letter_counter_dict[c] += 1
            else:
                letter_counter_dict[c] = 1
    for k,v in letter_counter_dict.items():
        if(v==1):
            target=k
    for s in array:
        if target in set(s.lower()):
            return s