from typing import List
import heapq


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        fac_primes = [0] * len(primes)
        k = [0] * n
        k[0] = 1
        for i in range(1, n):
            k[i] = min(k[fac_primes[j]] * primes[j] for j in range(len(primes)))
            for j in range(len(primes)):
                if k[i] == k[fac_primes[j]] * primes[j]:
                    fac_primes[j] += 1
        return k[n - 1]

    def nthSuperUglyNumber2(self, n: int, primes: List[int]) -> int:
        uglies = [1]

        def gen(prime):
            for ugly in uglies:
                yield ugly * prime

        merged = iter(heapq.merge(*map(gen, primes)))
        while len(uglies) < n:
            ugly = next(merged)
            if ugly != uglies[-1]:
                uglies.append(ugly)
        return uglies[-1]


if __name__ == '__main__':
    print(Solution().nthSuperUglyNumber2(n=12, primes=[2, 7, 13, 19]))
