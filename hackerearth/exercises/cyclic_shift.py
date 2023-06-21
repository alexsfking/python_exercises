
def cycle_binary_number(binary_num: int, num_digits: int) -> int:
    # Perform left shift operation to cycle the digits
    binary_num = ((binary_num << 1) | (binary_num >> (num_digits - 1))) & ((1 << num_digits) - 1)
    return binary_num

def calculate(binary_num:int,num_digits:int,k_max:int):
    maximum:int=binary_num
    max_count:int=1
    shift_count:int=0
    while(max_count<k_max and shift_count<num_digits):
        binary_num=cycle_binary_number(binary_num,num_digits)
        if(binary_num>maximum):
            maximum=binary_num
            max_count=1
        elif(binary_num==maximum):
            max_count+=1
        shift_count+=1
    return shift_count,max_count,maximum

def calculate_remaining_shifts(binary_num:int,maximum:int,num_digits:int,remaining_shifts:int):
    max_count:int=0
    shift_count:int=0
    while(max_count<remaining_shifts):
        binary_num=cycle_binary_number(binary_num,num_digits)
        if(binary_num==maximum):
            max_count+=1
        shift_count+=1
    return shift_count

def main():
    t_cases:int=int(input().strip())
    for _ in range(t_cases):
        n, k=map(int,input().split())
        a:int=int(input(),2)
        shift_count,max_count, maximum=calculate(a,n,k)
        #heuristic
        if(k>1000):
            multiplier, remainder=divmod(k,max_count)
            multiplier-=2
            remainder=k-multiplier*max_count
        else:
            multiplier=1
            remainder=k-max_count
        #print('shift_count,max_count,multiplier,remainder')
        #print(shift_count,max_count,multiplier,remainder)
        shift_count*=multiplier
        max_count*=multiplier
        shift_count+=calculate_remaining_shifts(a,maximum,n,remainder)
        #print('shift_count,max_count,multiplier,remainder')
        #print(shift_count,max_count,multiplier,remainder)
        print(shift_count)


if __name__ == "__main__":
    main()