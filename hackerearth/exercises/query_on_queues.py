'''
test case

1
20 20
4 2 8 3 5 9 11 1 13 14 15 12 7 6 19 20 18 17 16 10
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
'''

t_num_of_test_cases=int(input())
for _ in range(t_num_of_test_cases):
    n, k = map(int,input().split())
    queue = list(map(int,input().split()))
    x=[]
    for _ in range(k):
        x.append(int(input()))
    result_dict=dict()
    #calculate here
    for i in range(len(queue)):
        #left
        j=i-1
        while(j>-1 and queue[j]<queue[i]): 
            j-=1
        result_dict[i]=i-j
        #right
        j=i+1
        while(j<len(queue) and queue[i]>queue[j]): 
            j+=1
        result_dict[i]=result_dict[i]+j-i-1
    #output results here
    for case in x:
        print(result_dict.get(case-1))