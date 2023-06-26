t_cases:int=int(input())
for _ in range(t_cases):
    n_heights:int=int(input())
    heights_list:list[int]=list(map(int,input().split()))
    heights_dict=dict()
    for height in heights_list:
        if(height in heights_dict):
            heights_dict[height]+=1
        else:
            heights_dict[height]=1
    sorted_heights_by_mode=sorted(heights_dict.items(),key=lambda x: x[1],reverse=True)
    current_max=0
    for height_i,mode_i in sorted_heights_by_mode:
        for height_j,mode_j in reversed(sorted_heights_by_mode):
            if(height_i>height_j and mode_i>mode_j):
                if(current_max<mode_i-mode_j):
                    current_max=mode_i-mode_j
    if(current_max==0):
        current_max=-1
    print(current_max)