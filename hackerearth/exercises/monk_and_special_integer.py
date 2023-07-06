'''
Search
Use dyanmic sliding windows to find maxium subarrays less than x_max
x_max is the maximum sliding window sum
'''

n_size, x_max = map(int,input().split())
array_list:list = list(map(int,input().split()))

start,end,window_sum=0,0,0
size_set=False
window_max=len(array_list)

while(end<len(array_list)):
    window_sum+=array_list[end]
    window_size=end-start+1
    if(window_sum>x_max):
            #reduce the maximum winodw size
            window_sum=0
            window_max=window_size-1
            start,end=0,0
            continue
    end+=1
    if window_size == window_max:
        window_sum-=array_list[start]
        start+=1

print(window_max)