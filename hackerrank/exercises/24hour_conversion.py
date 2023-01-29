#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
# Given a time in 12-hour AM/PM format, convert it 
# to military (24-hour) time.
#

def timeConversion(s):
    # Write your code here
    #   hh  :   mm  :   ss   AM
    #   01  2   34  5   67   89
    twelve_hour=s[0:2]
    am_pm=s[8:]
    if(am_pm=="PM"):
        if(twelve_hour!="12"):
            twelve_hour=str(int(twelve_hour)+12)
    else:
        if(twelve_hour=="12"):
            twelve_hour="00"
    out=twelve_hour+s[2:8]
    return out

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
