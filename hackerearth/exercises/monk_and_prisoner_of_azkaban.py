'''
A[x]>A[i]
A[y]>A[i]
greatest x<i
smallest y>i
return x+y
if this is true for no x: x=-1
and likewise for y


'''
def build_stacks(array:list):
    x_stack=[]
    y_stack=[]
    for i in range(len(array_list)- 1, -1, -1):
        y_stack.append(array_list[i])
    return x_stack,y_stack

def get_x(stack:list,a_i:int,index:int):
    for i in range(len(stack)- 1, -1, -1):
        if(stack[i]>a_i):
            return i+1
    return -1

def get_y(stack:list,a_i:int,index:int):
    for i in range(len(stack)- 1, -1, -1):
        if(stack[i]>a_i):
            return len(stack)-i+index+1
    return -1


size=int(input())
array_list=list(map(int,input().split()))
x_stack,y_stack=build_stacks(array_list)
out=[]
#x_y=[]
for i in range(len(array_list)):
    middle=y_stack.pop()
    x=get_x(x_stack,array_list[i],i)
    y=get_y(y_stack,array_list[i],i)
    x_stack.append(middle)
    out.append(str(x+y))
    #x_y.append(str(x)+':'+str(y))

print(" ".join(out))
#print(" ".join(x_y))