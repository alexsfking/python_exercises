'''
A[x]>A[i]
A[y]>A[i]
greatest x<i
smallest y>i
return x+y
if this is true for no x: x=-1
and likewise for y

'''

size=int(input())
array_list=list(map(int,input().split()))
stack=[]
x_list=[]
stack.append((array_list[0],0))
x_list.append(-1)
# build x_list
for i in range(1,len(array_list)):
    while(stack and stack[-1][0]<=array_list[i]):
        stack.pop()
    if(stack):
        x_list.append(stack[-1][1]+1)
        stack.append((array_list[i],i))
    else:
        stack.append((array_list[i],i))
        x_list.append(-1)

# build y_list
stack=[]
stack.append((array_list[-1],len(array_list)-1))
x_list[-1]+=-1
for i in range(len(array_list)-2,-1,-1):
    while(stack and stack[-1][0]<=array_list[i]):
        stack.pop()
    if(stack):
        x_list[i]+=stack[-1][1]+1
        stack.append((array_list[i],i))
    else:
        stack.append((array_list[i],i))
        x_list[i]+=-1


for i, x in enumerate(x_list):
    if i > 0:
        print(' ', end='')
    print(x, end='')


