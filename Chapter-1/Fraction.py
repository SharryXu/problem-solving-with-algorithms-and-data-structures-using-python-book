def gcd(m, n):
    while m % n != 0:
        old_m, old_n = m, n
        m, n = old_n, old_m % old_n

    return n


class Fraction:
    def __init__(self, top, bottom) -> None:
        self.num = top
        self.den = bottom

    def __str__(self) -> str:
        return str(self.num) + "/" + str(self.den)

    def __add__(self, other_fraction: "Fraction"):
        new_num = self.num * other_fraction.den + self.den * other_fraction.num
        new_den = self.den * other_fraction.den

        common = gcd(new_num, new_den)

        return Fraction(new_num / common, new_den / common)

    def __eq__(self, other: "Fraction") -> bool:
        first_num = self.num * other.den
        second_num = self.den * other.num

        return first_num == second_num


a = Fraction(1, 4)
b = Fraction(1, 2)

print(a == b)
print(a + b)
