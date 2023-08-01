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

is_divisible = lambda x, p: x % p == 0

def calculate(p:int,q:int,some_list:list):
    count=0
    if(p<q):
        if(is_divisible(p,q)):
            for x in some_list:
                if(is_divisible(x,q)):
                    count+=1
        else:
            for x in some_list:
                if(is_divisible(x,p) or is_divisible(x,q)):
                    count+=1
    else:
        if(is_divisible(q,p)):
            for x in some_list:
                if(is_divisible(x,p)):
                    count+=1
        else:
            for x in some_list:
                if(is_divisible(x,q) or is_divisible(x,p)):
                    count+=1
    return count

length_a=int(input())
a_list=list(map(int,input().split()))
number_of_queries=int(input())
results_dict=dict()
for _ in range(number_of_queries):
    p,q=map(int,input().split())
    if((p,q) not in results_dict):
        results_dict[(p,q)]=calculate(p,q,a_list)
        results_dict[(q,p)]=results_dict[(p,q)]
    print(results_dict[(p,q)])
