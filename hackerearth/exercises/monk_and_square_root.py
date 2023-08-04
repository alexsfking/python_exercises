'''
Monk and Square Root
Given two integers N and M, help Monk find an integer X, such that X^2 % M == N and  0 <= X. If there are multiple values of X print smallest one. If there is no possible value of X print 1.

Note: Make sure you handle integer overflow.

Input:
First line consists of a single integer T denoting the number of test cases.
Each test case consists of a single line containing two space separated integers denoting N and M.

Output:
For each test case print the required answer.

Constraints:
1 <= T <= 100
0 <=N < M <= 10^6
'''
import math

num_cases=int(input().strip())
squares=[x**2 for x in range(0,500000)]
for _ in range(num_cases):
    n,m=map(int,input().strip().split())
    for i in range(int(math.floor(math.sqrt(n))),m//2+1):
        if(squares[i]%m==n):
            print(i)
            break
    else:
        print(-1)