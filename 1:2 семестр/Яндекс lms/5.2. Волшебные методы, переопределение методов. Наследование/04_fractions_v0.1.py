class Fraction:
    def __good_fraction(self, coords: tuple) -> int:
        a, b = coords[0], coords[1]
        while b:
            a, b = b, a % b
        return coords[0] // a, coords[1] // a

    def __init__(self, *coords) -> None:
        self.n, self.d = (
            self.__good_fraction(tuple(map(int, coords[0].split('/'))))
            if isinstance(coords[0], str)
            else self.__good_fraction(coords)
        )

    def numerator(self, number=None) -> int:
        if number is not None:
            self.n, self.d = self.__good_fraction(number, self.d)
        return self.n
    
    def denominator(self, number=None) -> int:
        if number is not None:
            self.n, self.d = self.__good_fraction(self.n, number)
        return self.d
    
    def __str__(self) -> str:
        return f"{self.n}/{self.d}"
    
    def __repr__(self) -> str:
        return f"Fraction({self.n}, {self.d})"


fraction = Fraction(3, 9)
print(fraction, repr(fraction))
fraction = Fraction('7/14')
print(fraction, repr(fraction))
