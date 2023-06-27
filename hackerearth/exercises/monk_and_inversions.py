'''
Chat-GPT

The code you provided calculates the count of pairs of elements in a 2D array (m_array) where the element in the first row and column is greater than the element in the second row and column.

Here's a step-by-step explanation of the code:

    Read the number of test cases (t_cases) from input.
    Start a loop that iterates t_cases times.
    Read the number of numbers (n_numbers) from input.
    Create an empty list m_array to store the 2D array.
    Start another loop that iterates n_numbers times.
        Read a line of numbers from input, split it, and convert each number to an integer using map(int, input().split()).
        Append the resulting list of integers (temp) to the m_array.
    Initialize a counter count to 0.
    Start nested loops to iterate over each element in m_array.
        The outer loop (i) iterates over the rows of the array.
        The inner loop (j) iterates over the columns of the array.
        The nested loops (k and m) iterate over the remaining rows and columns respectively.
    Check if the element at position (i, j) is greater than the element at position (k, m). If it is, increment the count variable.
    Print the final count after all iterations.

The code essentially compares each element in the 2D array with every other element that comes after it. If the condition m_array[i][j] > m_array[k][m] is satisfied, it means the element at position (i, j) is greater than the element at position (k, m), and the count is incremented.

The time complexity of this code is O(n^4), where n is the number of numbers in each row/column of the 2D array. This is because there are four nested loops, each iterating n_numbers or len(m_array) times.
'''

t_cases:int=int(input())
for _ in range(0,t_cases):
    n_numbers:int=int(input())
    m_array:list[int]=[]
    for _ in range(0,n_numbers):
        temp=list(map(int,input().split()))
        m_array.append(temp)
    count=0
    for i in range(len(m_array)):
        for j in range(len(m_array[0])):
            for k in range(i,len(m_array)):
                for m in range(j,len(m_array[0])):
                    if(m_array[i][j]>m_array[k][m]):
                        count+=1
    print(count)