
def cycle_binary_number(binary_num: int, num_digits: int) -> int:
    # Perform left shift operation to cycle the digits
    binary_num = ((binary_num << 1) | (binary_num >> (num_digits - 1))) & ((1 << num_digits) - 1)
    return binary_num

def find_max(binary_num: int, num_digits: int) -> int:
    maximum: int = binary_num
    for _ in range(0, num_digits):
        binary_num = cycle_binary_number(binary_num, num_digits)
        maximum = max(binary_num, maximum)
    return maximum


def calculate(binary_num:int,num_digits:int,k_max:int, maximum:int)-> tuple[int, int]:
    max_count:int=0
    shift_count:int=0
    if(binary_num==maximum):
        max_count+=1
    while(max_count<k_max and shift_count<num_digits):
        binary_num=cycle_binary_number(binary_num,num_digits)
        if(binary_num==maximum):
            max_count+=1
        shift_count+=1
    return shift_count, max_count

def calculate_remaining_shifts(binary_num:int,maximum:int,num_digits:int,remaining:int)->int:
    max_count:int=0
    shift_count:int=0
    while(max_count<remaining):
        binary_num=cycle_binary_number(binary_num,num_digits)
        if(binary_num==maximum):
            max_count+=1
        shift_count+=1
    return shift_count

def read_input() -> tuple[int, list[tuple[int, int]], list[int]]:
    t_cases:int = int(input().strip())
    test_cases:list[tuple[int, int]] = []
    binary_nums:list[int] = []
    for _ in range(t_cases):
        n, k = map(int, input().split())
        a = int(input(), 2)
        test_cases.append((n, k))
        binary_nums.append(a)
    return t_cases, test_cases, binary_nums

def apply_skip(a: int, maximum: int, k: int, max_count: int) -> tuple[int, int]:
    if k > 20:
        if a == maximum:
            max_count -= 1
        multiplier, remainder = divmod(k, max_count)
        multiplier -= 1
        remainder = k - multiplier * max_count
        if a == maximum:
            remainder -= 1
    else:
        multiplier = 1
        remainder = k - max_count
    return multiplier, remainder

def main():
    t_cases, test_cases, binary_nums = read_input()
    for i in range(t_cases):
        n, k = test_cases[i]
        a = binary_nums[i]
        maximum = find_max(a, n)
        shift_count, max_count = calculate(a, n, k, maximum)
        multiplier, remainder = apply_skip(a, maximum, k, max_count)
        shift_count*=multiplier
        max_count*=multiplier
        shift_count+=calculate_remaining_shifts(a,maximum,n,remainder)
        print(shift_count)


if __name__ == "__main__":
    main()