'''
test case

1
20 4
4 2 8 3 5 9 11 1 13 14 15 12 7 6 19 20 18 17 16 10
15
4
10
20
'''


t_num_of_test_cases=int(input())
for _ in range(t_num_of_test_cases):
    n, k = map(int,input().split())
    queue = list(map(int,input().split()))
    x=[]
    for _ in range(k):
        x.append(int(input()))
    result=dict()
    #calculate here
    for i in range(len(queue)):
        pass
    #output results here
    for case in x:
        print(dict.get(case))