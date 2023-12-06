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

def calculate(number:int) -> int:
    return str(number)[-1]

def last_digit(n1:int, n2:int) -> int:
    n1 = calculate(n1)
    n2 = calculate(n2)
    print(n1,n2)
    return 0


'''
    current_index = cycle_dict[base].index(base)
    calculated_index = (exponent - current_index) % len(cycle_dict[base])
    number = cycle_dict[base][calculated_index]
'''