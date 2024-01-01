'''
### kyu 6 ###
You are provided with a skeleton of the class 'Fraction', which accepts two
arguments (numerator, denominator).

EXAMPLE:
fraction1 = Fraction(4, 5)
Your task is to make this class string representable, and addable while keeping
the result in the minimum representation possible.

EXAMPLE:
print (fraction1 + Fraction(1, 8))
outputs: 37/40
NB: DON'T use the built_in class 'fractions.Fraction'

Enjoy!
'''

from math import gcd

class Fraction:
    def __init__(self, numerator, denominator):
        self.top = numerator
        self.bottom = denominator
    
    def __eq__(self, other:'Fraction') -> bool:
        first_num = self.top * other.bottom
        second_num = other.top * self.bottom
        return first_num == second_num
        
    def __str__(self) -> str:
        return f'{self.top}/{self.bottom}'
    
    def __add__(self, other:'Fraction') -> 'Fraction':
        denominator = self.bottom * other.bottom
        numerator1 = (denominator // self.bottom) * self.top
        numerator2 = (denominator // other.bottom) * other.top
        top, bot = Fraction.simplify_fraction(numerator1 + numerator2, denominator)
        return Fraction(top, bot)
    
    @staticmethod
    def simplify_fraction(numerator: int, denominator: int) -> tuple[int, int]:
        common_divisor = gcd(numerator, denominator)
        simplified_numerator = numerator // common_divisor
        simplified_denominator = denominator // common_divisor
        return simplified_numerator, simplified_denominator