'''
test case 1
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

'''
test case 2
1
25 25
708 170 595 368 105 732 474 441 401 906 560 737 166 780 521 520 7 428 948 874 4 627 285 401 844
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
21
22
23
24
25
'''

t_num_of_test_cases=int(input())
for _ in range(t_num_of_test_cases):
    n, k = map(int,input().split())
    queue = list(map(int,input().split()))
    test_cases=[]
    for _ in range(k):
        test_cases.append(int(input())-1)
    right_list=[0 for x in queue]
    left_list=[0 for x in queue]
    #calculate here
    stack=[]
    for i in range(len(queue)):
        #right
        segment_counter=0
        while(stack and queue[i]>stack[-1][0]):
            value, segments, index = stack.pop()
            segment_counter+=segments
            left_list[index]=i-index
        stack.append((queue[i],segment_counter+1,i))
        right_list[i]=segment_counter+1

    count=1
    while(stack):
        value, segments, index = stack.pop()
        left_list[index]=count
        count+=segments

    #output results here
    for case in test_cases:
        print(left_list[case]+right_list[case]-1)