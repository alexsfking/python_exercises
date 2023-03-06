#!/bin/python3
'''
This question is designed to help you get a better understanding of basic heap
operations.

There are 3 types of query:
    "1 v" - Add an element  to the heap. 
    "2 v" - Delete the element  from the heap. 
    "3" - Print the minimum of all the elements in the heap. NOTE: It is
    guaranteed that the element to be deleted will be there in the heap. Also,
    at any instant, only distinct elements will be in the heap.

Input Format The first line contains the number of queries, Q. Each of the next
Q lines contains one of the 3 types of query.

Constraints 1<=Q<=10^5 -10^9<=v<=10^9

Output Format For each query of type 3, print the minimum value on a single
line.
'''

'''
***Chat-GPT***
This code is also designed to handle the same 3 types of queries: adding an
element to the heap, deleting an element from the heap, and printing the minimum
value in the heap. However, it improves upon the previous code by using two heaps
instead of one.

This code implements a heap data structure and performs three types of
operations on it - adding an element to the heap, deleting an element from the
heap, and printing the minimum value in the heap. The code uses two heaps, one
for storing the elements in the heap and the other for storing the deleted
elements.

The time complexity of adding an element to the heap is O(log n), where n is the
size of the heap. This is because heapq.heappush() maintains the heap property
by ensuring that the newly added element is in the correct position in the heap.

The time complexity of deleting an element from the heap is also O(log n)
because heapq.heappush() and heapq.heappop() both have a time complexity of
O(log n). When deleting an element, the code adds it to the delete heap using
heappush().

The time complexity of printing the minimum value in the heap is O(log n), which
is the time complexity of heappop(). The code first checks if the minimum value
in the heap matches the minimum value in the delete heap. If they match, the
code removes both elements from their respective heaps. If they do not match,
the code only removes the minimum value from the heap.

Overall, the time complexity of the code is O(q log n), where q is the number of
queries and n is the size of the heap. This is because each query operation
(add, delete, or print minimum) has a time complexity of O(log n) due to the use
of heap data structure. The worst-case time complexity of the code is O(q log
n), which occurs when all the queries are add operations, and the heap size
increases to n.
'''

import heapq

if __name__ == '__main__':
    operations=[]
    heap=[]
    delete=[]
    queries=int(input().rstrip())
    for i in range(queries):
        operations.append(list(map(int,input().split())))

    for op in operations:
        match op[0]:
            case 1:
                # insert element to heap
                heapq.heappush(heap,op[1])
            case 2:
                # delete element from heap
                heapq.heappush(delete,op[1])
            case 3:
                # print min heap
                while delete and heap[0]==delete[0]:
                    heapq.heappop(delete)
                    heapq.heappop(heap)
                print(heap[0])
            case _:
                raise NotImplementedError("An unexpected error occured.", op[0])
        
    