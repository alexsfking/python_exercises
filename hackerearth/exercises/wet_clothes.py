n, m, g = list(map(int,input().split()))
rain_times_list:list[int]=list(map(int,input().split()))
drying_time_dict=dict()
for drying_time in list(map(int,input().split())):
    if(drying_time in drying_time_dict):
        drying_time_dict[drying_time]+=1
    else:
        drying_time_dict[drying_time]=1

max_diff=0
for i in range(len(rain_times_list) - 1):
    diff = rain_times_list[i + 1] - rain_times_list[i]
    if(diff>max_diff):
        max_diff=diff

clothes=0
for k,v in drying_time_dict.items():
    if(max_diff>=k):
        clothes+=v
print(clothes)
