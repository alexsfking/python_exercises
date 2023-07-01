n_size:int=int(input())
array_list:list[str]=input().split()
maximum_length=len(str(max(array_list)))
if(maximum_length<5):
    array_list = [x.zfill(5) for x in array_list]
    loops=1
else:
    quotient,remainder=divmod(maximum_length,5)
    array_list = [x.zfill(maximum_length+remainder) for x in array_list]
    loops=quotient
    if(remainder):
        loops+=1
for i in range(1,2):
    array_list = sorted(array_list, key=lambda x: str(x)[-5*i:])
    remove_leading_zeroes = [int(x) for x in array_list] 
    print(" ".join(map(str, remove_leading_zeroes)))

for i in range(2,loops+1):
    array_list = sorted(array_list, key=lambda x: str(x)[-5*i:-(5*(i-1))])
    remove_leading_zeroes = [int(x) for x in array_list] 
    print(" ".join(map(str, remove_leading_zeroes)))