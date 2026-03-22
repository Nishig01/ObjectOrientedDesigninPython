import math
class Vector:
    def __init__(self, x:float,y:float):
        self.x = x
        self.y = y

    def __add__(self, other): return Vector(self.x + other.x, self.y + other.y)
    def __sub__(self, other): return Vector(self.x - other.x, self.y - other.y)
    def __mul__(self, other): return Vector(self.x * other.x, self.y * other.y)

    # comparison
    def __eq__(self, other): return self.x == other.x and self.y == other.y
    def __lt__(self, other): return self.magnitude() < other.magnitude()

    #String
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    def __str__(self):
        return f"({self.x}, {self.y})"

    # Container behavior
    def __len__(self): return 2
    def __getitem__(self, idx):
        return (self.x, self.y)

    def __hash__(self):
        return hash(self.x, self.y)
    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

v1 = Vector(3,4)
v2 = Vector(5,6)
print(v1 + v2)
print(v1.magnitude())
print(v1 < v2)