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
The following code fails some tests because removing an element from the list requires O(n) time + heapify O(n)
'''
'''
***Chat-GPT***
The given code is a Python implementation for handling basic heap operations.
The program takes input from the user in the form of queries, and the output is
based on the type of query that is specified.

The program begins by importing the heapq module, which provides functions for
working with heaps. It then initializes two empty lists: operations to store the
user input and heap to store the elements of the heap.

The input format consists of Q queries, where Q is the number of queries. Each
query is one of three types:

    "1 v": Add an element v to the heap.
    "2 v": Delete the element v from the heap.
    "3": Print the minimum of all the elements in the heap.

The program then reads in the input and stores it in the operations list. Next,
it processes each query in the operations list one by one using a loop. For each
query, it matches the first element of the query with one of the cases:

    case 1: If the query is of type "1 v", the program adds the element v to the
    heap using the heappush function from the heapq module. 
    case 2: If the query is of type "2 v", the program removes the element v
    from the heap using the remove method of the heap list and then heapifies
    the list using the heapify function from the heapq module. Note that this
    implementation is inefficient because removing an element from the middle of
    a list requires O(n) time complexity.
    case 3: If the query is of type "3", the program prints the minimum value in
    the heap, which is always located at index 0 of the heap list.

If the first element of the query does not match any of the three cases, the
program raises a NotImplementedError with the message "An unexpected error
occurred."

However, the implementation of removing an element from the middle of a list and
then heapifying it using the heapify function is inefficient, as it has O(n)
time complexity. Therefore, this implementation may fail some tests
'''

import heapq

if __name__ == '__main__':
    operations=[]
    heap=[]
    queries=int(input().rstrip())
    for i in range(queries):
        operations.append(input().split())

    for op in operations:
        match op[0]:
            case 1:
                # insert element to heap
                heapq.heappush(heap,op[1])
            case 2:
                # delete element from heap
                heap.remove(op[1])
                heapq.heapify(heap)
            case 3:
                # print min heap
                print(heap[0])
            case _:
                raise NotImplementedError("An unexpected error occured.")
        
    