def count_elements(query_type:int,query_value:int,array_list:list)->int:
    count:int=0
    if(query_type==1):
        for elem in array_list:
            if(elem>query_value):
                count+=1
    else:
        for elem in array_list:
            if(elem<=query_value):
                count+=1
    return count

n_size=int(input())
array_list:list=map(int,input().split())
q_size=int(input())
query_dict=dict()
for _ in range(q_size):
    query_type, query_value=map(int,input().split())
    if((query_type,query_value) not in query_dict):
        query_dict[(query_type,query_value)]=count_elements(query_type,query_value,array_list)
    print(query_dict[(query_type,query_value)])


