from sympy import symbols, Poly

class PolynomialProcessor:
    def __init__(self):
        self.x = symbols('x')

    def extended_euclidean_algorithm(self, a, b):
        a, b = Poly(a, self.x), Poly(b, self.x)
        old_r, r = a, b
        old_s, s = Poly(1, self.x), Poly(0, self.x)
        old_t, t = Poly(0, self.x), Poly(1, self.x)

        while r:
            quotient = old_r // r
            old_r, r = r, old_r - quotient * r
            old_s, s = s, old_s - quotient * s
            old_t, t = t, old_t - quotient * t

        return old_r, old_s, old_t
