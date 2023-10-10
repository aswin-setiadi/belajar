class Solution:
    """
    using dfs, bottom up approach
    """

    def climb_stairs(self, n: int) -> int:
        one, two = 1, 1

        for _ in range(n - 1):
            temp = one
            one = one + two
            two = temp

        return one


def main():
    print(Solution().climb_stairs(5))


if __name__ == "__main__":
    main()
