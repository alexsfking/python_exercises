'''
### kyu 5 ###
Complete the solution so that it returns the number of times the search_text is
found within the full_text.

search_substr( full_text, search_text, allow_overlap = True )
so that overlapping solutions are (not) counted. If the searchText is empty, it
should return 0.

Usage examples:
search_substr('aa_bb_cc_dd_bb_e', 'bb') # should return 2 since bb shows up twice
search_substr('aaabbbcccc', 'bbb') # should return 1
search_substr( 'aaa', 'aa' ) # should return 2
search_substr( 'aaa', '' ) # should return 0
search_substr( 'aaa', 'aa', False ) # should return 1
'''

import re

def search_substr(full_text:str, search_text:str, allow_overlap:bool = True) -> int:
    if search_text == '': return 0
    if not allow_overlap:
        return len(re.findall(search_text,full_text))
    return len(re.findall(f'(?=({search_text}))',full_text))