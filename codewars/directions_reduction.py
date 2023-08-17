class Directions():
    def __init__(self) -> None:
        self.north_south_set=set(["NORTH", "SOUTH"])
        self.east_west_set=set(["EAST", "WEST"])

    def is_oppostite(self,a,b):
        return a != b and {a, b} in [self.north_south_set, self.east_west_set]


def dirReduc(arr):
    direction_stack=[]
    dir=Directions()
    for direction in arr:
        if(len(direction_stack)):
            if(dir.is_oppostite(direction,direction_stack[-1])):
                direction_stack.pop()
            else:
                direction_stack.append(direction)
        else:
            direction_stack.append(direction)
    return direction_stack

a = ["NORTH", "WEST", "SOUTH", "EAST"]
print(dirReduc(a))