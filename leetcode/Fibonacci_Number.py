class Solution:
    def fib(self, n: int) -> int:
        F = [0 for i in range(n + 1)]
        F[0], F[1] = 0, 1

        for i in range(2, n + 1):
            F[i] = F[i - 2] + F[i - 1]

        return F[n]