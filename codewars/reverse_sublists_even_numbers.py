def rev_sub(arr):
    rev,out=[],[]
    for value in arr:
        if(value%2==0):
            rev.append(value)
        else:
            while(len(rev)):
                out.append(rev.pop())
            out.append(value)
    while(len(rev)):
        out.append(rev.pop())
    return out

print(rev_sub([2,4,3]))