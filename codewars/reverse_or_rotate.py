'''
### kyu 6 ###
The input is a string str of digits. Cut the string into chunks (a chunk here is
a substring of the initial string) of size sz (ignore the last chunk if its size
is less than sz).

If a chunk represents an integer such as the sum of the cubes of its digits is
divisible by 2, reverse that chunk; otherwise rotate it to the left by one
position. Put together these modified chunks and return the result as a string.

If

sz is <= 0 or if str is empty return ""
sz is greater (>) than the length of str it is impossible to take a chunk of
size sz hence return "".

Examples:
revrot("123456987654", 6) --> "234561876549"
revrot("123456987653", 6) --> "234561356789"
revrot("66443875", 4) --> "44668753"
revrot("66443875", 8) --> "64438756"
revrot("664438769", 8) --> "67834466"
revrot("123456779", 8) --> "23456771"
revrot("", 8) --> ""
revrot("123456779", 0) --> "" 
revrot("563000655734469485", 4) --> "0365065073456944"
Example of a string rotated to the left by one position:
s = "123456" gives "234561".
'''

def rotate_string(some_string:str) -> str:
    if some_string:
        some_string = some_string[1:] + some_string[0]
    return some_string

def rev_rot(input_string:str, sz:int) -> str:
    if sz <= 0 or input_string == "" or sz > len(input_string): return ""
    num_chunks = len(input_string) // sz
    chunks = [input_string[i * sz : (i + 1) * sz] for i in range(num_chunks)]
    for i, chunk in enumerate(chunks):
        total = 0
        for c in chunk:
            total += pow(int(c),3)
        if total % 2: chunks[i] = rotate_string(chunk)
        else: chunks[i] = chunk[::-1]
    return ''.join(chunks)

s = "733049910872815764"
print(rev_rot(s, 5) == "330479108928157")