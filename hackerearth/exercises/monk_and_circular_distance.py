'''
report the number of points lying inside or on the circumference of this circle.
Each query is a radius for a circle
'''

'''
***Chat-GPT***
This code is designed to calculate the number of points lying inside or on the
circumference of a given circle. It takes input in the following format:

    The first input represents the number of points, num_points, and is an integer
    value. The next num_points lines represent the coordinates of the points. Each
    line contains two space-separated integers representing the x and y coordinates
    of a point. The next input is an integer value, num_queries, representing the
    number of queries. The next num_queries lines represent the radius of the
    circles for which the number of points inside or on the circumference needs to
    be calculated. Each line contains a single integer representing the radius.

The code performs the following steps:

The get_inputs() function is defined to retrieve the necessary inputs. It reads the number of points, coordinates of the points, number of queries, and the radii of the circles.
The squared_distance_list is created by calculating the squared distance of each point from the origin (0,0) using the coordinates provided. The squared distance is calculated as x * x + y * y for each point. The list is then sorted in ascending order.
The inside_circle_dict dictionary is initialized to store the count of points inside or on the circumference of each circle. The keys represent the radii of the circles, and the values are initially set to 0.
For each radius r in the queries list:

    If the count for that radius has not been previously calculated and stored in
    inside_circle_dict, the calculation is performed. The squared value of the
    radius, r_squared, is calculated. The count in inside_circle_dict for the radius
    r is set to 0 (to be updated later). A binary search is performed on the
    squared_distance_list to find the index of the boundary where the squared
    distance is greater than r_squared.
        If the squared distance at the middle index is less than or equal to
        r_squared, it means the point at that index is inside the circle or on the
        circumference. Therefore, the search continues in the upper half. If the
        squared distance at the middle index is greater than r_squared, it means the
        point at that index is outside the circle. Therefore, the search continues
        in the lower half.
    The binary search continues until the lower and upper bounds meet (low > high).
    The count of points inside the circle is determined by the index of the
    boundary, which is stored in inside_circle_dict[r]. The count is printed.

The code essentially uses binary search to efficiently find the number of points
lying inside or on the circumference of a circle for a given radius, based on
the precalculated squared distances of the points from the origin. This approach
avoids the need to calculate the actual distances and directly works with
squared distances for comparison.
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