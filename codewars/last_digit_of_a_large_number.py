'''
### kyu 5 ###
Define a function that takes in two non-negative integers a and b and returns the last decimal digit of a^b. Note that a and b may be very large!

Examples
last_digit(4, 1)                # returns 4
last_digit(4, 2)                # returns 6
last_digit(9, 7)                # returns 9
last_digit(10, 10 ** 10)        # returns 0
last_digit(2 ** 200, 2 ** 300)  # returns 6
'''

cycle_dict = {
    0: [0],
    1: [1],
    2: [4, 8, 6, 2],
    3: [9, 7, 1, 3],
    4: [6, 4],
    5: [5],
    6: [6],
    7: [9, 3, 1, 7],
    8: [4, 2, 6, 8],
    9: [1, 9]
}

def last_digit(n1:int, n2:int) -> int:
    if n2 == 0: return 1
    last_digit_n1 = int(str(n1)[-1])
    current_index = cycle_dict[last_digit_n1].index(last_digit_n1)
    calculated_index = (n2 - 1 + current_index) % len(cycle_dict[last_digit_n1])
    return cycle_dict[last_digit_n1][calculated_index]


for n1, n2, exp in [
                    (4, 1, 4),
                    (4, 2, 6),
                    (9, 7, 9),
                    (10, 10 ** 10, 0),
                    (2 ** 200, 2 ** 300, 6),
                    (3715290469715693021198967285016729344580685479654510946723, 68819615221552997273737174557165657483427362207517952651, 7)]:
    print(last_digit(n1, n2) == exp, f"Testing last_digit({n1}, {n2})")

'''
    current_index = cycle_dict[base].index(base)
    calculated_index = (exponent - current_index) % len(cycle_dict[base])
    number = cycle_dict[base][calculated_index]
'''