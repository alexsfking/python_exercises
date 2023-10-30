def snail(snail_map:list[list[int]])->list[int]:
    min_row,min_col,max_row,max_col,out = 0,0,len(snail_map)-1,len(snail_map[0])-1,[]
    while(min_row<=max_row and min_col<=max_col): #clockwise
        for i in range(min_col,max_col+1): #top
            out.append(snail_map[min_row][i])
        min_row+=1
        for i in range(min_row,max_row+1): #right
            out.append(snail_map[i][max_col])
        max_col-=1
        for i in range(max_col,min_col-1,-1): #bottom
            out.append(snail_map[max_row][i])
        max_row-=1
        for i in range(max_row,min_row-1,-1): #left
            out.append(snail_map[i][min_col])
        min_col+=1
    return out


array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
expected = [1,2,3,4,5,6,7,8,9]
print(snail(array) == expected)