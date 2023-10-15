class SolutionAswin:
    """50.44% 45.77%"""

    @staticmethod
    def fib(n: int) -> int:
        tmp1 = 0
        tmp2 = 1
        if n == 0:
            return tmp1
        elif n == 1:
            return tmp2
        else:
            for _ in range(2, n + 1):
                total = tmp1 + tmp2
                tmp1 = tmp2
                tmp2 = total
            return total


class Solution:
    @staticmethod
    def fib(n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a


def main():
    ans = Solution.fib(5)
    print(ans)


if __name__ == "__main__":
    main()
