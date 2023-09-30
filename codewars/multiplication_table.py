def multiplication_table(size):
    out=[]
    for i in range(1,size+1):
        row=[]
        for j in range(1,size+1):
            row.append(j*i)
        out.append(row)
    return out