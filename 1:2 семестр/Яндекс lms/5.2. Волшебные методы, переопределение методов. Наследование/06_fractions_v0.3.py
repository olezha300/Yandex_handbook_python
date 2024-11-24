class Fraction:
    def __good_fraction(self, coords):
        a, b = coords[0], coords[1]
        while b:
            a, b = b, a % b
        return coords[0] // a, coords[1] // a

    def __init__(self, *coords):
        self.n, self.d = (
            self.__good_fraction(tuple(map(int, coords[0].split("/"))))
            if isinstance(coords[0], str)
            else self.__good_fraction(coords)
        )

    def numerator(self, number=None):
        if number is not None:
            if self.n > 0:
                self.n, self.d = self.__good_fraction((abs(number), self.d))
                self.n = -self.n if number < 0 else self.n
            elif self.n < 0:
                self.n, self.d = self.__good_fraction((abs(number), self.d))
                self.n = -self.n if number > 0 else self.n
        return abs(self.n)

    def denominator(self, number=None):
        if number is not None:
            if self.n > 0:
                self.n, self.d = self.__good_fraction((self.n, abs(number)))
                self.n = -self.n if number < 0 else self.n
            elif self.n < 0:
                self.n, self.d = self.__good_fraction((abs(self.n), abs(number)))
                self.n = -self.n if number > 0 else self.n
        return self.d

    def __neg__(self):
        return Fraction(-self.n, self.d)

    def __add__(self, other):
        return Fraction(self.n * other.d + other.n * self.d, self.d * other.d)

    def __iadd__(self, other):
        self.n, self.d = self.__good_fraction(
            (self.n * other.d + other.n * self.d, self.d * other.d)
        )
        return self

    def __sub__(self, other):
        return Fraction(self.n * other.d - other.n * self.d, self.d * other.d)

    def __isub__(self, other):
        self.n, self.d = self.__good_fraction(
            (self.n * other.d - other.n * self.d, self.d * other.d)
        )
        return self

    def __str__(self):
        return f"{self.n}/{self.d}"

    def __repr__(self):
        return f"Fraction('{self.n}/{self.d}')"
