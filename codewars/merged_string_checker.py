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
    i,j,k = 0,0,0
    while i<len(part1) and j<len(part2) and k<len(string):
        if string[k] == part1[i]:
            i +=1
            k +=1
        elif string[k] == part2[j]:
            j +=1
            k +=1
        else:
            return False
    return True