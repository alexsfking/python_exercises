#return smallest number bigger than a target
def smallest_larger_number(numbers, target):
    smallest_larger = None
    for num in numbers:
        if num > target:
            if smallest_larger is None or num < smallest_larger:
                smallest_larger = num
    return smallest_larger


def next_bigger(n):
    number_list = [int(digit) for digit in str(n)]
    for i in range(len(number_list) - 1, 0, -1):
        if(number_list[i]>number_list[i-1]):
            temp=number_list[i-1]
            next_smallest=smallest_larger_number(number_list[i:],temp)
            for j in range(len(number_list) - 1, -1, -1):
                if(number_list[j]==next_smallest):
                    number_list[j]=temp
                    break
            number_list[i-1]=next_smallest
            out=int(''.join(map(str, number_list[0:i]+sorted(number_list[i:]))))
            if(number_list[0]==0):
                break
            return out
    return(-1)

print(next_bigger(12345626666543)==12345632456666)