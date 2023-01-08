#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#
# Julius Caesar protected his confidential information by encrypting it using a cipher. 
# Caesar's cipher shifts each letter by a number of letters. If the shift takes you 
# past the end of the alphabet, just rotate back to the front of the alphabet. 
# In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.
#

def caesarCipher(s, k):
    # Write your code here
    letters=[chr(i) for i in range(ord('a'),ord('z')+1)]
    out=[]
    for character in s:
        if(character.isalpha()):
            if(character.lower()!=character):
                value=ord(character.lower())-ord('a')+k
                if(value>25):
                    value%=26
                out.append(letters[value].upper())
            else:
                value=ord(character)-ord('a')+k
                if(value>25):
                    value%=26
                out.append(letters[value])
        else:
            out.append(character)
    return "".join(out)
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
