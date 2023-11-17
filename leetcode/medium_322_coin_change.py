class Solution:
    """neetcode answer"""

    def __init__(self, arr: list[int], amt: int) -> None:
        self.arr = arr
        self.amt = amt
        self.coins: int = -1

    def solve(self):
        dp = [self.amt + 1] * (self.amt + 1)
        dp[0] = 0
        for a in range(1, self.amt + 1):
            for c in self.arr:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[self.amt] if dp[self.amt] != self.amt + 1 else -1


def main():
    ans = Solution([6, 2, 5], 11).solve()
    print(f"ans={ans} real ans=3")


if __name__ == "__main__":
    main()
