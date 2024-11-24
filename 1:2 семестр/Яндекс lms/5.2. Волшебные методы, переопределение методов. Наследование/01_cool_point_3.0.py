# Классная точка 3.0

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def move(self, distance_x, distance_y):
        self.x += distance_x
        self.y += distance_y
    
    def length(self, point):
        return round(((point.x - self.x) ** 2 + (point.y - self.y) ** 2) ** 0.5, 2)


class PatchedPoint(Point):
    def __init__(self, *coords):
        if len(coords) == 0:
            self.x, self.y = 0, 0
        elif len(coords) == 1:
            self.x, self.y = coords[0][0], coords[0][1]
        else:
            self.x, self.y = coords[0], coords[1]


first_point = PatchedPoint((2, -7))
second_point = PatchedPoint(7, 9)
print(first_point.length(second_point))
print(second_point.length(first_point))
