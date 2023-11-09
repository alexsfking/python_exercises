def loop_size(start_node:object)->int:
    current_node=start_node
    visited_dict=dict()
    count = 0
    while(current_node not in visited_dict):
        visited_dict[current_node] = count
        current_node=current_node.next
        count += 1
    return count - visited_dict[current_node]