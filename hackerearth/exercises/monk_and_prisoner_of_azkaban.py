'''
A[x]>A[i]
A[y]>A[i]
greatest x<i
smallest y>i
return x+y
if this is true for no x: x=-1
and likewise for y
'''

'''
***Chat-GPT***

This code takes an input list of integers and performs the following operations:

1. It reads the size of the list from the user and reads the list elements.

2. It initializes an empty stack and a list called `x_list` to store the values
   of `x`.

3. It pushes the first element of the list along with its index (0) onto the
   stack and sets `x_list[0]` to -1.

4. It iterates over the remaining elements of the list (starting from index 1)
    and performs the following steps:
    - It pops elements from the stack as long as the top element is smaller than or
        equal to the current element.
    - If the stack is not empty, it appends the index of the top element plus 1 to
        `x_list` and pushes the current element and its index onto the stack.
    - If the stack is empty, it pushes the current element and its index onto the
        stack and appends -1 to `x_list`.

5. After the above loop, the `x_list` will contain the values of `x` for each
   element in the list.

6. Next, it initializes the stack again.

7. It pushes the last element of the list along with its index onto the stack
   and subtracts 1 from `x_list[-1]`.

8. It iterates over the elements of the list in reverse order (starting from the
   second-to-last element) and performs similar steps as in step 4:
    - It pops elements from the stack as long as the top element is smaller than or
        equal to the current element.
    - If the stack is not empty, it adds the index of the top element plus 1 to the
        corresponding element in `x_list`.
    - If the stack is empty, it pushes the current element and its index onto the
        stack and subtracts 1 from the corresponding element in `x_list`.

9. After the above loop, the `x_list` will contain the sum of `x` and `y` for each element in the list.

10. Finally, it prints the values in `x_list` separated by spaces.
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


