t_cases:int=int(input())
for _ in range(t_cases):
    n_heights:int=int(input())
    heights_dict=dict()
    for height in map(int,input().split()):
        heights_dict[height] = heights_dict.get(height, 0) + 1
    sorted_heights_by_heights=sorted(heights_dict.items(),key=lambda x: x[0])
    
    min_freq=float('inf')
    difference=0
    for height_i, freq_i in sorted_heights_by_heights:
        if min_freq>freq_i:
            min_freq=freq_i
        else:
            difference=max(difference,freq_i-min_freq)        

    if(difference==0):
        difference=-1
    print(difference)