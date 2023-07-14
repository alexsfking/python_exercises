'''
The first line consists of two space separated integers N and X, denoting the
number of spiders in the queue and the number of spiders that have to be
selected respectively.

The next line consists of an array A, Ai denoting the power of spider at
position i (1<=i<=n).

For each of the X iterations, output the position of the selected spider in that
iteration. Position refers to the index at which the spider was present in the
initial given queue (1 based indexing).
'''

from collections import deque

n_spiders, x_selected=list(map(int,input().split()))
a_list=list(map(int,input().split()))
#make the list a tuple
a_list = [(value, i) for i, value in enumerate(a_list)]

a_deque:deque=deque(a_list)
out=[]
requeue=[]
for iterations in (range(x_selected)):
    max_value=-1
    count=0
    index=-1
    condition=min(x_selected,len(a_deque))
    while(a_deque and count<condition):
        value,index=a_deque.popleft()
        if(value>max_value):
            max_value=value
            max_index=count
        if(value>0):
            value-=1
        requeue.append((value,index))
        count+=1
    out.append(str(requeue.pop(max_index)[1]+1))
    a_deque.extend(requeue)
    requeue.clear()

print(" ".join(out))
