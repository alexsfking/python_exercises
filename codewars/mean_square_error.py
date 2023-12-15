'''
### kyu 5 ###
Complete the function that

accepts two integer arrays of equal length
compares the value each member in one array to the corresponding member in the other
squares the absolute value difference between those two values
and returns the average of those squared absolute value difference between each member pair.
Examples
[1, 2, 3], [4, 5, 6]              -->   9   because (9 + 9 + 9) / 3
[10, 20, 10, 2], [10, 25, 5, -2]  -->  16.5 because (0 + 25 + 25 + 16) / 4
[-1, 0], [0, -1]                  -->   1   because (1 + 1) / 2

[(10-10)^2, (25-20)^2, (10-5)^2 ...
'''

def solution(array_a:list[int], array_b:list[int]) -> float:
    sum = 0
    for i in range(len(array_a)):
        sum += pow(array_b[i] - array_a[i], 2)
    return sum / len(array_a)