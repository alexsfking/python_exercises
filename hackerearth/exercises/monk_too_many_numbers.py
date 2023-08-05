'''

'''
def get_inputs():
    n,m=map(int,input().strip().split())
    l,r=map(int,input().strip().split())
    k=int(input().strip())
    return n,m,l,r,k

def create_array(n,m,l,r,k):
    b=n%m
    out=[]
    for i in range(l,m):
        if((n % i)==b):
            out.append(i)
            if(len(out)>k):
                return None

    for i in range(m+1,r):
        if((n % i)==b):
            out.append(i)
            if(len(out)>k):
                return None
    return out


n,m,l,r,k=get_inputs()
out=create_array(n,m,l,r,k)
if(out!=None):
    print(len(out))
    print(" ".join(str(value) for value in out))
else:
    print(-1)