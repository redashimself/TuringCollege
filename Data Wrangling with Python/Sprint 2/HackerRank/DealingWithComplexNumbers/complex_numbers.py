# https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/problem


class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        return Complex(self.real + no.real, self.imaginary + no.imaginary)

    def __sub__(self, no):
        return Complex(self.real - no.real, self.imaginary - no.imaginary)

    def __mul__(self, no):
        real_part = self.real * no.real - self.imaginary * no.imaginary

        imaginary_part = self.real * no.imaginary + self.imaginary * no.real
        return Complex(real_part, imaginary_part)

    def __truediv__(self, no):
        denominator = no.real ** 2 + no.imaginary ** 2
        real_part = (self.real * no.real + self.imaginary * no.imaginary) / denominator
        imaginary_part = (self.imaginary * no.real - self.real * no.imaginary) / denominator
        return Complex(real_part, imaginary_part)

    def mod(self):
        modulus = (self.real ** 2 + self.imaginary ** 2) ** 0.5
        return Complex(modulus, 0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result


def parse_complex(s):
    parts = s.split()
    return Complex(float(parts[0]), float(parts[1]))


if __name__ == '__main__':
    c = input()
    d = input()
    x = parse_complex(c)
    y = parse_complex(d)
    print(*map(str, [x + y, x - y, x * y, x / y, x.mod(), y.mod()]), sep='\n')
