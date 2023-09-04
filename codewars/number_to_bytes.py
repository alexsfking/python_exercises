'''
In this kata, your task is to write a function to_bytes(n) (or toBytes(n)
depending on language) that produces a list of bytes that represent a given
non-negative integer n. Each byte in the list is represented by a string of '0'
and '1' of length 8. The most significant byte is first in the list. The example
test cases should provide you with all the details. You may assume that the
argument n is valid.
'''

def to_bytes(n):
    temp = bin(n)[2:]
    padding_zeroes=(8-len(temp)%8)%8
    temp='0'*padding_zeroes+temp
    out=[temp[i:i+8] for i in range(0,len(temp),8)]
    return out