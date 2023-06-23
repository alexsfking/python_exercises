num_strings:int=int(input())
array:list[str]=[]
for _ in range(num_strings):
    line=input()
    array.append(line)
    array.sort()
    print(array.index(line))
