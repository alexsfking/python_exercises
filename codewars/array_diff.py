def array_diff(a, b):
    out=[]
    b_set=set(b)
    for value in a:
        if(value not in b_set):
            out.append(value)
    return out