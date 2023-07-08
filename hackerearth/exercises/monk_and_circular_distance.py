'''
report the number of points lying inside or on the circumference of this circle.
Each query is a radius for a circle
'''
def get_inputs():
    num_points=int(input())
    coords=[]
    for _ in range(num_points):
        coords.append(list(map(int,input().split())))
    num_queries=int(input())
    queries=[]
    for _ in range(num_queries):
        queries.append(int(input()))
    return num_points,coords,num_queries,queries


num_points,coords,num_queries,queries=get_inputs()
squared_distance_list = sorted([x * x + y * y for x, y in coords])
#lets record some past calculations in inside_circle_dict
inside_circle_dict=dict()
for r in queries:
    if r not in inside_circle_dict:
        r_squared=r*r
        inside_circle_dict[r]=0
        # Perform binary search for the boundary
        low = 0
        high = len(squared_distance_list) - 1
        while low <= high:
            mid = (low + high) // 2

            if squared_distance_list[mid] <= r_squared:
                # The point at mid is inside the circle or on the circumference,
                # so we search in the upper half
                low = mid + 1
            else:
                # The point at mid is outside the circle,
                # so we search in the lower half
                high = mid - 1

        # The count of points inside the circle is the index of the boundary
        inside_circle_dict[r] = low
    print(inside_circle_dict[r])