# Классный прямоугольник

class Rectangle:
    
    def __init__(self, first_tuple: tuple, second_tuple: tuple) -> None:
        self.first_tuple = first_tuple
        self.second_tuple = second_tuple
    
    def perimeter(self) -> float:
        a = abs(self.second_tuple[0] - self.first_tuple[0])
        b = abs(self.second_tuple[1] - self.first_tuple[1])
        return round(2 * (a + b), 2)
    
    def area(self) -> float:
        a = abs(self.second_tuple[0] - self.first_tuple[0])
        b = abs(self.second_tuple[1] - self.first_tuple[1])
        return round(a * b, 2)


rect = Rectangle((3.2, -4.3), (7.52, 3.14))
print(rect.perimeter())
rect = Rectangle((7.52, -4.3), (3.2, 3.14))
print(rect.area())
