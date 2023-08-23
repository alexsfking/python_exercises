

def solution(number):
    number-=1
    if(number<3):
        return 0
    three=number//3
    sum_three=three/2*(3+three*3)
    five=number//5
    sum_five = (five / 2 * (5 + five * 5)) if number > 4 else 0
    three_five=number//15
    sum_three_five = (three_five / 2) * (15 + three_five * 15) if number > 14 else 0
    return sum_three+sum_five-sum_three_five

print(solution(6))