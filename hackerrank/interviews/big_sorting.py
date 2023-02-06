"""
Consider an array of numeric strings where each string is a positive number with anywhere from to digits. Sort the array's elements in non-decreasing, or ascending order of their integer values and return the
sorted array.

Example
    unsorted=['1','200','150','3']

    Return the array ['1', '3', '150', '200'].

Function Description
    Complete the bigSorting function in the editor below.
    
    bigSorting has the following parameter(s):
        string unsorted[n]: an unsorted array of integers as strings

Returns
    string[n]: the array sorted in numerical order
"""
#
# Complete the 'bigSorting' function below.
#
# The f nction is e pected to ret rn a STRING ARRAY
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY unsorted as parameter.
#
def string_sort(string:str):
    return int(string)

def bigSorting(unsorted):
    # Write your code here
    return sorted(unsorted,key=string_sort)