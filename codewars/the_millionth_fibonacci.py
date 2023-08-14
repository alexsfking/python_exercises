fib_list=[0,1,1]

def calculate(n):
    for i in range(len(fib_list),n+1):
        fib_list.append(fib_list[i-1]+fib_list[i-2])


def get_negative(n):
    return -fib_list[-n] if n % 2 == 0 else fib_list[-n]

def fib(n):
    if(n>-1 and n<len(fib_list)):
        return fib_list[n]
    calculate(-n) if n<0 else calculate(n)
    if(n<0):
        return get_negative(n)
    return fib_list[n]

