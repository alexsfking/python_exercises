def calc_sum(number,divisor):
    quotient=number//divisor
    sum_divisor = (quotient / 2 * (divisor + quotient * divisor)) if number > divisor-1 else 0
    return sum_divisor

def solution(number):
    number-=1
    if(number<3):
        return 0
    sum_three = calc_sum(number,3)
    sum_five = calc_sum(number,5)
    sum_three_five = calc_sum(number,15)
    return sum_three+sum_five-sum_three_five

print(solution(6))