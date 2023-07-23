'''
***Chat-GPT***

The given code is a Python program that takes an input `num_strings`,
representing the number of strings to be entered, followed by `num_strings`
lines of text input. It then stores the input strings in a list named `array`,
sorts the list in alphabetical order, and finally, it prints the index of each
input string in the sorted array.

Let's break down the code step by step:

1. `num_strings:int=int(input())`: This line takes user input and stores it in
   the variable `num_strings`. It explicitly specifies that the input should be
   an integer by using the type hint `int`.

2. `array:list[str]=[]`: This line initializes an empty list named `array` that
   will be used to store the input strings. It also specifies that the elements
   of the list should be of type `str` using the type hint `list[str]`.

3. `for _ in range(num_strings):`: This line starts a loop that will iterate
   `num_strings` times. The loop is represented by the variable `_`, which is a
   common convention in Python when you don't actually need the loop variable.

4. `line=input()`: Within the loop, this line takes user input and stores it in
   the variable `line`. Each input string is read and processed one by one.

5. `array.append(line)`: This line appends the current input string (stored in
   `line`) to the list `array`.

6. `array.sort()`: After each input string is appended to the list, this line
   sorts the `array` in alphabetical order. Sorting is necessary to get the
   correct index later.

7. `print(array.index(line))`: This line prints the index of the current input
   string (`line`) in the sorted `array`. The `index()` method is used to find
   the position of `line` within the list. It will return the index of the first
   occurrence of the string in the list.

Note: It's worth mentioning that using `array.sort()` inside the loop may not be
the most efficient approach, especially if you have a large number of strings.
Sorting the array repeatedly for each input string can be costly in terms of
time complexity. A more efficient approach would be to store the input strings
in the list and sort it once after the loop has finished. Then, you can find the
indices of the original input strings using a different method like a dictionary
to map each string to its original index. However, as this is just a simple
explanation of the given code, it doesn't delve into optimization
considerations.
'''

num_strings:int=int(input())
array:list[str]=[]
for _ in range(num_strings):
    line=input()
    array.append(line)
    array.sort()
    print(array.index(line))
