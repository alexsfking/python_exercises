#!/bin/python3

import math
import os
import random
import re
import sys

"""
Sherlock considers a string to be valid if all characters of the string appear the same number of times.
It is also valid if he can remove just 1 character at 1 index in the string, and the remaining characters 
will occur the same number of times. Given a string s, determine if it is valid. If so, return YES, 
otherwise return NO.

    # 3,3   4,1 = good
    # 3,3   3,1 = good
    # 3,3   2,1 = bad
    # 3,3   1,1 = good
    # 3,1   2,2 = good
    # 4,1   2,2 = bad
    # 2,1   2,2 = good

"""

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def calculate_repeating_characters(s:str)->dict():
    character_occurrence_dict=dict()
    for c in s:
        if(c not in character_occurrence_dict):
            character_occurrence_dict[c]=1
        else:
            character_occurrence_dict[c]+=1
    return character_occurrence_dict

def calculate_repeating_values(character_occurrence_dict:dict)->dict():
    value_occurrence_dict=dict()
    for k,v in character_occurrence_dict.items():
        if(v not in value_occurrence_dict):
            value_occurrence_dict[v]=1
        else:
            value_occurrence_dict[v]+=1
    return value_occurrence_dict

def check_conditions(value_occurrence_dict:dict)->str:
    failing="NO"
    passing="YES"
    if(len(value_occurrence_dict)>2):
        #too many values
        return failing
    elif(len(value_occurrence_dict)==1):
        #only one value
        return passing
    #exactly two values
    d_keys=[]
    d_values=[]
    for k,v in value_occurrence_dict.items():
        d_keys.append(k)
        d_values.append(v)
    if(d_values[1]==1):
        if(d_keys[1]==d_keys[0] or d_keys[0]+1==d_keys[1]):
            return passing
        if(d_keys[1]==1):
            return passing
    if(d_values[0]==1):
        if(d_keys[1]==d_keys[0] or d_keys[0]==d_keys[1]+1):
            return passing
        if(d_keys[0]==1):
            return passing
    return failing

def isValid(s):
    # Write your code here
    character_occurrence_dict=calculate_repeating_characters(s)
    value_occurrence_dict=calculate_repeating_values(character_occurrence_dict)
    out=check_conditions(value_occurrence_dict)
    return out

if __name__ == '__main__':
    print(isValid("a"))
    print(isValid("aaaaabc"))
    print(isValid("ibfdgaeadiaefgbhbdghhhbgdfgeiccbiehhfcggchgghadhdhagfbahhddgghbdehidbibaeaagaeeigffcebfbaieggabcfbiiedcabfihchdfabifahcbhagccbdfifhghcadfiadeeaheeddddiecaicbgigccageicehfdhdgafaddhffadigfhhcaedcedecafeacbdacgfgfeeibgaiffdehigebhhehiaahfidibccdcdagifgaihacihadecgifihbebffebdfbchbgigeccahgihbcbcaggebaaafgfedbfgagfediddghdgbgehhhifhgcedechahidcbchebheihaadbbbiaiccededchdagfhccfdefigfibifabeiaccghcegfbcghaefifbachebaacbhbfgfddeceababbacgffbagidebeadfihaefefegbghgddbbgddeehgfbhafbccidebgehifafgbghafacgfdccgifdcbbbidfifhdaibgigebigaedeaaiadegfefbhacgddhchgcbgcaeaieiegiffchbgbebgbehbbfcebciiagacaiechdigbgbghefcahgbhfibhedaeeiffebdiabcifgccdefabccdghehfibfiifdaicfedagahhdcbhbicdgibgcedieihcichadgchgbdcdagaihebbabhibcihicadgadfcihdheefbhffiageddhgahaidfdhhdbgciiaciegchiiebfbcbhaeagccfhbfhaddagnfieihghfbaggiffbbfbecgaiiidccdceadbbdfgigibgcgchafccdchgifdeieicbaididhfcfdedbhaadedfageigfdehgcdaecaebebebfcieaecfagfdieaefdiedbcadchabhebgehiidfcgahcdhcdhgchhiiheffiifeegcfdgbdeffhgeghdfhbfbifgidcafbfcd"))

'''                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()

'''