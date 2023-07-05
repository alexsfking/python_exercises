import bisect

def create_search_table(array_list:list)->dict:
    search_dict=dict()
    for i in range(len(array_list)):
        if(array_list[i] in search_dict):
            search_dict[array_list[i]]['counter']+=1
        else:
            search_dict[array_list[i]] = {'index': i, 'counter': 1}
    return search_dict

def count_elements(query_type: int, query_value: int, array_list: list, search_dict: dict) -> int:
    if query_value in search_dict:
        index=search_dict[query_value]['index']
        counter=search_dict[query_value]['counter']
        if query_type == 1:
            return index
        else:
            return index + counter
    count = 0
    if query_type == 1:
        #>
        index = bisect.bisect_right(array_list, query_value)
        count = len(array_list) - index
    else:
        #>=
        index = bisect.bisect_left(array_list, query_value)
        count = len(array_list) - index
    return count

n_size=int(input())
array_list:list=sorted(list(map(int,input().split())),reverse=True)
search_dict=create_search_table(array_list)
array_list.reverse()
q_size=int(input())
query_dict=dict()
for _ in range(q_size):
    query_type, query_value=map(int,input().split())
    if((query_type,query_value) not in query_dict):
        query_dict[(query_type,query_value)]=count_elements(query_type,query_value,array_list,search_dict)
    print(query_dict[(query_type,query_value)])


