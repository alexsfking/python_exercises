def narcissistic(value:int)->bool:
    value_str=str(value)
    exponent=len(value_str)
    total=0
    for c in value_str:
        total+=pow(int(c),exponent)
    if(total==value):
        return True
    return False

print(narcissistic(7)==True)
print(narcissistic(371)==True)
print(narcissistic(122)==False)
print(narcissistic(4887)==False)