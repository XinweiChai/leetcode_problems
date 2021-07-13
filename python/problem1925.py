from math import isqrt, gcd


class Solution:
    # Euclid's formula: a = m^2 - n^2, b = 2mn, c = m^2 + n^2, and find coprimes (m, n) and (m, n) one odd one even
    def countTriples(self, n: int) -> int:
        root = isqrt(n)
        return 2 * sum(n // (x ** 2 + y ** 2) for x in range(1, root + 1) for y in range(x + 1, root + 1) if
                       (x & y & 1) == 0 and gcd(x, y) == 1)
