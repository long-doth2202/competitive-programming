class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def fact(v):
            if (v == 1):
                return 1
            return v * fact(v - 1)

        if (n == 1 or m == 1):
            return 1

        p = fact((m - 1) + (n - 1))
        q = fact(m - 1) * fact(n - 1)

        return p // q