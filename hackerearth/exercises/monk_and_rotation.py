t_int:int=int(input().strip())
for i in range(0,t_int):
    n_int,k_int=map(int,input().split())
    a_list:list[int]=list(map(int,input().split()))
    k_int=k_int%n_int
    start_index=n_int-k_int
    out=[]
    for j in range(start_index,n_int):
        out.append(a_list[j])
    if(start_index!=0):
        for j in range(0,start_index):
            out.append(a_list[j])
    print(" ".join(str(num) for num in out))