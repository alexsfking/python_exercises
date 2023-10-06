def encode(st:str):
    count=1
    last=st[0]
    out=[]
    for i in range(1,len(st)):
        if(st[i]==last):
            count+=1
        else:
            out.append(str(count)+last)
            count=1
            last=st[i]
    out.append(str(count)+last)
    return ''.join(out)


def decode(st:str): 
    out=[]
    digit_index=None
    for i in range(0,len(st)):
        if(st[i].isdigit()):
            if(digit_index==None):
                digit_index=i
        else:
            out.append(int(st[digit_index:i])*st[i])
            digit_index=None
    return ''.join(out)


print(decode (encode ("AAAAAAAAAAB")), "AAAAAAAAAAB")