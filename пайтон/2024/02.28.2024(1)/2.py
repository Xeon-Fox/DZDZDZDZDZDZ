from functools import lru_cache

class MathOperations:
    @staticmethod
    @lru_cache(maxsize=None)
    def factorial(n):
        if n < 2:
            return 1
        return n * MathOperations.factorial(n-1)

math_ops = MathOperations()
print(math_ops.factorial(5))