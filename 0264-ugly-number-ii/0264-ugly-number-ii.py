class Solution:
    def nthUglyNumber(self, n: int) -> int:
        primes = [2, 3, 5]
        indices = [0, 0, 0]
        uglies = [1]

        for _ in range(1, n):
            next_vals = [primes[i] * uglies[indices[i]] for i in range(3)]
            next_ugly = min(next_vals)
            uglies.append(next_ugly)

            for i in range(3):
                if next_vals[i] == next_ugly:
                    indices[i] += 1

        return uglies[-1]