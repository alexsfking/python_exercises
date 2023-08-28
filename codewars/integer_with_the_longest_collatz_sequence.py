collatz_dict={2: 1, 1: 0}

def calculate_collatz(value:int)->int:
    if(value%2):
        return(3*value+1)
    return value//2

def longest_collatz(input_array:list)->int:
    global collatz_dict
    current_max=0
    index_of_max=0
    for i in range(len(input_array)):
        element=input_array[i]
        stack=[]
        while element not in collatz_dict: #calculate
            stack.append(element)
            element=calculate_collatz(element)
        count=1
        while(stack): #add results to dict
            collatz_dict[stack.pop()]=collatz_dict[element]+count
            count+=1
        if collatz_dict[input_array[i]] > current_max: #check > max
            current_max=collatz_dict[input_array[i]]
            index_of_max=i
    return input_array[index_of_max]

print(longest_collatz([1, 5, 27, 4]))