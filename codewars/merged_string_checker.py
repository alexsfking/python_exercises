'''
### kyu 5 ###
At a job interview, you are challenged to write an algorithm to check if a given
string, s, can be formed from two other strings, part1 and part2.

The restriction is that the characters in part1 and part2 should be in the same
order as in s.

The interviewer gives you the following example and tells you to figure out the
rest from the given test cases.

For example:

'codewars' is a merge from 'cdw' and 'oears':

    s:  c o d e w a r s   = codewars
part1:  c   d   w         = cdw
part2:    o   e   a r s   = oears
'''

def is_merge(string:str, part1:str, part2:str)->bool:
    if not string and not part1 and not part2: return True
    if not string: return False

    if part1 and string[0] == part1[0]:
        if is_merge(string[1:], part1[1:], part2): return True
    if part2 and string[0] == part2[0]:
        if is_merge(string[1:], part1, part2[1:]): return True

    return False

print(is_merge('codewars', 'code', 'wars') == True)
print(is_merge('codewars', 'cdw', 'oears') == True)
print(is_merge('codewars', 'cod', 'wars') == False)
print(is_merge("Bananas from Bahamas", "Bahas", "Bananas from am") == True)
