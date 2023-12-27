'''
### kyu 5 ###
Create a class Vector that has simple (3D) vector operators.

In your class, you should support the following operations, given Vector a and Vector b:

a + b # returns a new Vector that is the resultant of adding them
a - b # same, but with subtraction
a == b # returns true if they have the same magnitude and direction
a.cross(b) # returns a new Vector that is the cross product of a and b
a.dot(b) # returns a number that is the dot product of a and b
a.to_tuple() # returns a tuple representation of the vector.
str(a) # returns a string representation of the vector in the form "<a, b, c>"
a.magnitude # returns a number that is the magnitude (geometric length) of vector a.
a.x # gets x component
a.y # gets y component
a.z # gets z component
Vector([a,b,c]) # creates a new Vector from the supplied 3D array.
Vector(a,b,c) # same as above
The test cases will not mutate the produced Vector objects, so don't worry about that.
'''

class Vector:
    def __init__(self, *args) -> None:
        if len(args) == 1 and isinstance(args[0], (list, tuple)) and len(args[0]) == 3:
            # If a single argument is given and it's a list or tuple of length 3, use it as the array
            values = list(args[0])
        elif len(args) == 3:
            # If three arguments are given, use them as individual values
            values = list(args)
        else:
            raise ValueError("Invalid input. Provide either a 3D array or three individual values.")
        self.x = values[0]
        self.y = values[1]
        self.z = values[2]
    
    def __add__(self, other:'Vector') -> 'Vector':
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other:'Vector') -> 'Vector':
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __eq__(self, other:'Vector') -> bool:
        return self.x == other.x and self.y == other.y and self.z == other.z
    
    def __str__(self) -> str:
        return f'<{self.x}, {self.y}, {self.z}>'
    
    def to_tuple(self) -> tuple:
        return tuple([self.x,self.y,self.z])
    
    @property
    def magnitude(self) -> float:
        return pow(pow(self.x, 2) + pow(self.y, 2) + pow(self.z, 2), 0.5)
    
    def cross(self, other:'Vector') -> 'Vector':
        return Vector(self.y * other.z - self.z * other.y, 
                      self.z * other.x - self.x * other.z,
                      self.x * other.y - self.y * other.x)

    def dot(self, other:'Vector') -> int:
        return self.x * other.x + self.y * other.y + self.z * other.z
    
examples = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
vectors = []
for v in examples:
    vectors.append(Vector(v))
    print(vectors[-1].to_tuple())
    print(vectors[-1] + vectors[-1])
    print(vectors[-1] - vectors[-1])
    print(vectors[-1] == vectors[-1])
    print(vectors[-1].magnitude)