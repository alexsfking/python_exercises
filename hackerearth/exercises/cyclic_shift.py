
def cycle_binary_number(binary_num: int, num_digits: int) -> int:
    # Perform left shift operation to cycle the digits
    binary_num = ((binary_num << 1) | (binary_num >> (num_digits - 1))) & ((1 << num_digits) - 1)
    return binary_num

t_cases:int=int(input().strip())
for _ in range(t_cases):
    n, k=map(int,input().split())
    a:int=int(input(),2)
    maximum:int=a
    max_count:int=1
    shift_count:int=0
    while(max_count<k):
        a=cycle_binary_number(a,n)
        if(a>maximum):
            maximum=a
            max_count=1
        elif(a==maximum):
            max_count+=1
        shift_count+=1

    print(shift_count)
