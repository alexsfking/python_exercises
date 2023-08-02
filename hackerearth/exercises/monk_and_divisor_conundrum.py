'''
Monk and Divisor Conundrum
Here is another task for you, prepared by Monk himself. So, this is how it goes:

Given an integer array A of size N, Monk needs you to answer T queries for him.
In each query, he gives you 2 integers P and Q. In response to each of these
queries, you need to tell Monk the count of numbers in array A. that are either
divisible by P, Q, or both.

Can you cope with this ?

Input Format :

The first line contains a single integer N denoting the size of array A. The
next line contains N space separated integers, where the ith integer denotes
A[i].

The next line contains a single integer T denoting the number of queries Monk
poses to you. Each of the next T lines contains 2 space separated integers P and
Q.

Output Format :
For each query, print the answer on a new line.
'''

import math

lcm = lambda a, b: a*b // math.gcd(a, b)

length_a=int(input().strip())
a_list=list(map(int,input().strip().split()))
maximum=max(a_list)+1

freq=[0 for _ in range(maximum+1)]
for value in a_list:
    freq[value]+=1

div=[0 for _ in range(maximum+1)]
for i in range(1,maximum):
    for factor in range(i,maximum+1, i):
        div[i]+=freq[factor]

number_of_queries=int(input().strip())
for _ in range(number_of_queries):
    p,q=map(int,input().strip().split())
    pq=lcm(p,q)
    a=div[p] if p<=maximum else 0
    b=div[q] if q<=maximum else 0
    ab=div[pq] if pq<=maximum else 0
    print(a+b-ab)