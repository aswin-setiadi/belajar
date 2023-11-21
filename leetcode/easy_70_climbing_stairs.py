class Solution:
    """
    using dfs, bottom up approach
    neetcode answer
    """

    def climb_stairs(self, n: int) -> int:
        one, two = 1, 1

        for _ in range(n - 1):
            temp = one
            one = one + two
            two = temp

        return one

    def climb_stairs1(self, n: int) -> int:
        """colin answers recursive and iterative
        https://www.youtube.com/watch?v=Clp5c7HvLqs
        """

        def rec(index: int) -> int:
            if index == 0:
                return 1
            if ans[index] != -1:
                return ans[index]
            cur = 0
            if index - 1 >= 0:
                cur += rec(index - 1)
            if index - 2 >= 0:
                cur += rec(index - 2)
            ans[index] = cur
            return cur

        ans = [-1] * (n + 1)
        return rec(n)

    def climb_stairs2(self, n: int) -> int:
        ans = [0] * (n + 1)
        ans[0] = 1
        for i in range(n):
            if i + 1 <= n:
                ans[i + 1] += ans[i]
            if i + 2 <= n:
                ans[i + 2] += ans[i]
        return ans[-1]


def main():
    print(Solution().climb_stairs(5))
    print(Solution().climb_stairs1(5))
    print(Solution().climb_stairs2(5))


if __name__ == "__main__":
    main()
