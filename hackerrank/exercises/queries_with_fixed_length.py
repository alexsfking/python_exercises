#!/bin/python3

import math
import os
import random
import re
import sys

'''
Consider an n-integer sequence, A = {a0,a1,...,an-1 }. We perform a query on A
by using an integer, d, to calculate the result of the following expression: 

    min(max aj)
    0<=i<=n-d	i<=j<i+d

In other words, if we let mi = max(ai,ai+1,..,ai+d-1), then you need to
calculate min(m0,m1,..,mn-d) Given arr and q queries, return a list of answers
to each query.

Example
arr = [2,3,4,5, 6]
queries = [2,3]
The first query uses all of the subarrays of length 2: [2, 3], [3, 4], [4, 5],
[5, 6]. The maxima of the subarrays are [3, 4, 5, 6]. The minimum of these is 3.
The second query uses all of the subarrays of length 3: [2, 3, 4], [3, 4, 5],
(4, 5, 6]. The maxima of the subarrays are [4, 5, 6]. The minimum of these is 4.
Return [3, 4].

Function Description
Complete the solve function below.
solve has the following parameter(s):
* int arr[n]: an array of integers
* int queries[q]: the lengths of subarrays to query
Returns
* int[q]: the answers to each query

Input Format.
The first line consists of two space-separated integers, n and q. The second
line consists of n space-separated integers, the elements of arr. Each of the q
subsequent lines contains a single integer denoting the value of d for that
query.

Constraints
1<=n<=10^5
0<=arr[i]<=10^6
1<=q<=100
1<=d<=n
'''

'''
***Chat-GPT***
The solve function takes in two arguments, an array arr of integers and an array
queries of integers. It returns an array of integers representing the minimum of
the maximum values of all subarrays of arr with lengths equal to the elements in
queries.

The function loops through each element in queries and performs the following
steps for each query:

    1. Initializes an empty list window_max_list to store the maximum values of
       all subarrays of arr with length equal to the current query value.
    2. Initializes a deque window_indices to store the indices of elements in
       the current sliding window.
    3. Loops through each element in arr using a sliding window approach.
    4. Removes indices of elements that are outside the current sliding window
       from the deque.
    5. Removes indices of elements that are smaller than the current element
       from the deque.
    6. Appends the index of the current element to the deque.
    7. If the window has reached the desired size, appends the maximum value to
       the window_max_list.
    8. Appends the minimum value of the window_max_list to the output list out.
    9. Returns out after all queries have been processed.

The function uses a sliding window approach to efficiently compute the maximum
values of all subarrays of arr with a given length. It also uses a deque to
store the indices of elements in the sliding window, allowing for efficient
removal of elements outside the current window and smaller than the current
element. Finally, it uses the built-in min function to compute the minimum value
of the maximum values of each subarray.

Are there any improvements we can make to solve to make it more efficient?

Yes, there are a few potential improvements we can make to the solve function to
make it more efficient:

    1. Pre-compute the maximum values for each subarray of length d before
    iterating over them. This can be done using a sliding window algorithm
    similar to the one used in the max_sliding_window function.

    2. Use a data structure like a min heap to store the maximum values for each
    subarray. This can reduce the time complexity of finding the minimum value
    from O(qnlog n) to O(q*log n).

    3. Use memoization to store the maximum values for previously computed
    subarrays, so that we don't have to recompute them again. This can reduce
    the time complexity of finding the maximum values from O(qn) to O(n + qk),
    where k is the number of unique subarray lengths in the queries array.
    However, this improvement may not be useful if queries contains a large
    number of unique values.

Overall, the most promising improvement would likely be pre-computing the
maximum values for each subarray using a sliding window algorithm, since this
can reduce the time complexity of finding the maximum values from O(qn) to O(n +
q(n-d+1)), which is much faster for large values of n and small values of d.

Here's an implementation of solve that precomputes the maximum values for each
subarray using a sliding window algorithm:

def solve(arr, queries):
    n = len(arr)
    
    # Precompute maximum values for each subarray of length d
    max_vals = []
    for d in range(1, n + 1):
        window_max_list = []
        window_indices = deque()
        for window_end in range(len(arr)):
            # Remove indices of elements that are outside the current sliding window
            while window_indices and window_indices[0] <= window_end - d:
                window_indices.popleft()
            # Remove indices of elements that are smaller than the current element
            while window_indices and arr[window_indices[-1]] < arr[window_end]:
                window_indices.pop()
            # Add the index of the current element to the deque
            window_indices.append(window_end)
            # If the window has reached the desired size, append the maximum value to the list
            if window_end >= d - 1:
                window_max_list.append(arr[window_indices[0]])
        max_vals.append(window_max_list)

    # For each query, find the minimum of the precomputed maximum values
    out = []
    for q in queries:
        out.append(min(max_vals[q-1]))

    return out

In this implementation, we first precompute the maximum values for each subarray
of length d (where d ranges from 1 to n). We store these maximum values in a
list of lists called max_vals, where max_vals[d-1] contains the maximum values
for all subarrays of length d.

To compute the maximum values, we use a sliding window algorithm similar to the
one used in the original implementation. The main difference is that we iterate
over all possible subarrays of length d, rather than sliding a window of size d
over the array. For each subarray, we maintain a deque of indices representing
the elements in the subarray that might be the maximum. We update this deque as
we iterate over the array, adding new indices to the back and removing old
indices from the front. Once the deque contains the indices of the maximum
elements in the subarray, we append the maximum element to a list of maximum
values for that subarray.

Finally, for each query, we look up the precomputed maximum values for subarrays
of length q and return the minimum value.

This implementation has a time complexity of O(n^2), which is the same as the
original implementation. However, it has the advantage of precomputing the
maximum values for each subarray, which can make the code faster if there are
many queries on subarrays of similar lengths.
'''
#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY queries
#

from collections import deque

def solve(arr, queries):
    # Write your code here
    out=[]
    for q in queries:
        window_max_list=[]
        window_indices=deque()
        for window_end in range(len(arr)):
            # Remove indices of elements that are outside the current sliding window
            while window_indices and window_indices[0]<=window_end-q:
                window_indices.popleft()
            # Remove indices of elements that are smaller than the current element
            while(window_indices and arr[window_indices[-1]]<arr[window_end]):
                window_indices.pop()
            # Add the index of the current element to the deque
            window_indices.append(window_end)

            # If the window has reached the desired size, append the maximum value to the list
            if window_end >= q - 1:
                window_max_list.append(arr[window_indices[0]])
        out.append(min(window_max_list))
    return out

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = solve(arr, queries)

    #fptr.write('\n'.join(map(str, result)))
    #fptr.write('\n')

    #fptr.close()
