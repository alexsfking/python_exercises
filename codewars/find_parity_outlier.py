def find_outlier(integers):
    odd,even=0,0
    last_odd,last_even=None,None
    for i,integer in enumerate(integers):
        if(integer%2):
            odd+=1
            last_odd=integer
        else:
            even+=1
            last_even=integer
        if(i>1 and odd and even):
            if(odd<even):
                return last_odd
            return last_even
    return None