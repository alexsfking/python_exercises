'''
Search
Use dynamic sliding windows to find maximum subarrays less than x_max
x_max is the maximum sliding window sum
'''

n_size, x_max = map(int,input().split())
array_list:list = list(map(int,input().split()))

start,end,window_sum=0,0,0
window_max=len(array_list)

while(end<len(array_list)):
    window_sum+=array_list[end]
    window_size=end-start+1
    if(window_sum>x_max):
            #reduce the maximum window size
            window_sum-=(array_list[end]+array_list[end-1])
            window_max=window_size-1
            end-=1
            continue
    end+=1
    if window_size == window_max:
        window_sum-=array_list[start]
        start+=1

print(window_max)


'''
***Chat-GPT***
This code is an implementation of a sliding window algorithm to find the maximum
subarrays whose sum is less than a given value x_max. Here's a breakdown of how
the code works:

    The first line of code reads two integers n_size and x_max from the input.
    n_size represents the size of the array, and x_max is the maximum sliding window
    sum allowed.

    The second line reads a list of integers array_list from the input. This is the
    input array on which we will perform the sliding window algorithm.

    The variables start, end, and window_sum are initialized to 0. start and end
    represent the indices of the sliding window, and window_sum keeps track of the
    sum of the elements within the window.

    The variable window_max is initialized to the length of the input array
    array_list. This variable represents the maximum window size encountered so far.

    The while loop iterates as long as the end index is less than the length of
    array_list.

    Inside the loop, the current element array_list[end] is added to the window_sum.
    Then, the window_size is calculated as end - start + 1, which represents the
    size of the current window.

    If the window_sum exceeds x_max, it means the current window sum is too large.
    In this case, the algorithm reduces the window size by subtracting the last two
    elements from window_sum and updating window_max to window_size - 1. The end
    index is also decremented by 1 to keep the window size consistent.

    If the window_sum is still less than or equal to x_max, the end index is
    incremented by 1 to expand the window.

    After expanding the window, the algorithm checks if the window_size is equal to
    window_max. If they are equal, it means the current window is the largest
    encountered so far. In this case, the algorithm subtracts the first element
    array_list[start] from window_sum and increments the start index by 1 to slide
    the window.

    Finally, after the while loop completes, the algorithm outputs the value of
    window_max, which represents the maximum window size among all the subarrays
    whose sum is less than x_max.

In summary, this code finds the maximum subarrays with a sum less than x_max
using a sliding window approach. It starts with a small window and expands it
until the sum exceeds the threshold, at which point it reduces the window size
and continues. The algorithm keeps track of the maximum window size encountered
and outputs it at the end.
'''