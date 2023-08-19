'''
ROT13 is a simple letter substitution cipher that replaces a letter with the
letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar
cipher.

Create a function that takes a string and returns the string ciphered with
Rot13. If there are numbers or special characters included in the string, they
should be returned as they are. Only letters from the latin/english alphabet
should be shifted, like in the original Rot13 "implementation".

Please note that using encode is considered cheating.
'''

def rot13(message:str):
    out=[]
    for c in message:
        if(c.isalpha()):
            base = ord('A') if c.isupper() else ord('a')
            rotated = (ord(c) - base + 13) % 26 + base
            out.append(chr(rotated))
        else:
            out.append(c)
    return "".join(out)