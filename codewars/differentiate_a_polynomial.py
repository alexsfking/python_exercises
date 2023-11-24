'''
### kyu 4 ###
Create a function that differentiates a polynomial for a given value of x.

Your function will receive 2 arguments: a polynomial as a string, and a point to evaluate the equation as an integer.

Assumptions:
There will be a coefficient near each x, unless the coefficient equals 1 or -1.
There will be an exponent near each x, unless the exponent equals 0 or 1.
All exponents will be greater or equal to zero
Examples:
differenatiate("12x+2", 3)      ==>   returns 12
differenatiate("x^2+3x+2", 3)   ==>   returns 9
'''

import re

term_pattern = re.compile(r'''
                          (?P<sign>[\+\-]?)
                          (?P<coefficient>[0-9]*)
                          (?P<variables>[a-z]+)
                          [\^]?
                          (?P<exponent>[0-9]*)
                          ''',re.VERBOSE)

def differentiate(equation:str, point:int)->int:
    terms = term_pattern.findall(equation)
    result=0
    for term in terms:
        sign = -1 if term[0] == '-' else 1
        coefficient = int(term[1] or '1')
        coefficient *= sign
        exponent = int(term[3] or '1')
        coefficient *= exponent
        exponent -= 1
        result += coefficient * pow(point,exponent)
    return result