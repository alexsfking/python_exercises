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
x_list.append('-1')
# build x_list
for i in range(1,len(array_list)):
    while(stack and stack[-1][0]<=array_list[i]):
        stack.pop()
    if(stack):
        stack.append((array_list[i],stack[-1][1]+1))
        x_list.append(stack[-1][1]+1)
    else:
        stack.append((array_list[i],i))
        x_list.append(-1)

# build y_list
stack=[]
y_list=[]
stack.append((array_list[-1],len(array_list)-1))
for i in range(len(array_list)-1,-1,-1):
    while(stack and stack[-1][0]<=array_list[i]):
        stack.pop()
    if(stack):
        stack.append((array_list[i],stack[-1][1]+1))
        y_list.append(stack[-1][1]+1)
    else:
        stack.append((array_list[i],i))
        y_list.append(-1)

out=[]
for i in range(len(x_list)):
    out.append(str(x_list[i]+y_list[i]))

print(" ".join(out))

