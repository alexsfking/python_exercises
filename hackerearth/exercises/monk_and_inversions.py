t_cases:int=int(input())
for _ in range(0,t_cases):
    n_numbers:int=int(input())
    m_array:list[int]=[]
    for _ in range(0,n_numbers):
        temp=list(map(int,input().split()))
        m_array.append(temp)
    count=0
    for i in range(len(m_array)):
        for j in range(len(m_array[0])):
            for k in range(i,len(m_array)):
                for m in range(j,len(m_array[0])):
                    if(m_array[i][j]>m_array[k][m]):
                        count+=1
    print(count)