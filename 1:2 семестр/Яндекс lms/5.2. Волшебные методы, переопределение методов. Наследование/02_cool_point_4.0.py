# Классная точка 4.0

class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    
    def move(self, distance_x, distance_y) -> None:
        self.x += distance_x
        self.y += distance_y
    
    def length(self, point) -> float:
        return round(((point.x - self.x) ** 2 + (point.y - self.y) ** 2) ** 0.5, 2)


class PatchedPoint(Point):
    def __init__(self, *coords: tuple) -> None:
        if len(coords) == 0:
            self.x, self.y = 0, 0
        elif len(coords) == 1:
            self.x, self.y = coords[0][0], coords[0][1]
        else:
            self.x, self.y = coords[0], coords[1]
    
    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"PatchedPoint({self.x}, {self.y})"


first_point = PatchedPoint((2, -7))
second_point = PatchedPoint(7, 9)
print(*map(str, (first_point, second_point)))
print(*map(repr, (first_point, second_point)))
