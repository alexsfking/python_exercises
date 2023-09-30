def largest_smaller_number(numbers, target):
    largest_smaller = None
    for num in numbers:
        if num < target and (largest_smaller is None or num > largest_smaller):
            largest_smaller = num
    return largest_smaller

def next_smaller(n):
    number_list = [int(digit) for digit in str(n)]
    for i in range(len(number_list) - 1, 0, -1):
        if(number_list[i]<number_list[i-1]):
            temp=number_list[i-1]
            next_smallest=largest_smaller_number(number_list[i:],temp)
            for j in range(len(number_list) - 1, -1, -1):
                if(number_list[j]==next_smallest):
                    number_list[j]=temp
                    break
            number_list[i-1]=next_smallest
            out=int(''.join(map(str, number_list[0:i]+sorted(number_list[i:],reverse=True))))
            if(number_list[0]==0):
                break
            return out
    return(-1)