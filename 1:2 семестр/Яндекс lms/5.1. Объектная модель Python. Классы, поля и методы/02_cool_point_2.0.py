# Классная точка 2.0

class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def move(self, distance_x, distance_y):
        self.x += distance_x
        self.y += distance_y
    
    def length(self, point):
        return round(((point.x - self.x) ** 2 + (point.y - self.y) ** 2) ** 0.5, 2)


point = Point(3, 5)
print(point.x, point.y)
point.move(2, -3)
print(point.x, point.y)
