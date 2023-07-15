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

'''
***Chat-GPT***
This code is used to select the positions of spiders from a queue based on their
power. Here's a breakdown of how it works:

1. The first line of code reads two space-separated integers, `N` and `X`, from
   the input. These represent the number of spiders in the queue and the number
   of spiders that need to be selected, respectively.

2. The second line of code reads an array `A` from the input. The array `A`
   represents the power of each spider at a specific position in the queue.

3. The next few lines convert the array `A` into a list of tuples, where each
   tuple contains the power of the spider and its corresponding index in the
   queue. This conversion is done to keep track of the spider's original
   position even after sorting or manipulating the queue.

4. A deque (double-ended queue) named `a_deque` is created using the converted
   list `a_list`.

5. Two empty lists, `out` and `requeue`, are initialized. `out` will store the
   positions of the selected spiders, and `requeue` will temporarily hold
   spiders that are not selected in each iteration.

6. A loop iterates `x_selected` number of times, representing the number of
   spiders to be selected.

7. Within each iteration, the code finds the spider with the maximum power in
   the current queue. It keeps track of the maximum power (`max_value`), the
   index of the spider with maximum power (`max_index`), and the count of
   iterations (`count`).

8. The code then iterates through the `a_deque` queue while there are still
   spiders in it and the count is less than the minimum value between
   `x_selected` and the length of `a_deque`.

9. In each iteration of the inner loop, the code retrieves the value and index
   of the spider from the left side of the queue using `a_deque.popleft()`. It
   updates the `max_value` and `max_index` if the current spider has a higher
   power.

10. After updating the maximum values, the code decreases the power of the
    spider by 1 if it is greater than 0.

11. The updated spider (with reduced power) is appended to the `requeue` list.

12. The count is incremented, and the inner loop continues until the exit
    condition is met.

13. Once the inner loop ends, the code selects the spider with the maximum power
    (using `requeue.pop(max_index)`) and appends its original position (`[1]`)
    to the `out` list.

14. The `requeue` list is then extended back into the `a_deque` queue.

15. Finally, the `out` list is printed, with each position separated by a space.

In summary, this code simulates selecting spiders from a queue based on their
power and prints the positions of the selected spiders in each iteration. The
spiders' powers are reduced by 1 after each iteration.
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
