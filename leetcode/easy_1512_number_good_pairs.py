from collections import Counter


class Solution:
    # speed 32.94%, memory 82.24%
    def numIdenticalPairs(self, nums: list[int]) -> int:
        return sum([sum(range(v)) for _, v in Counter(nums).items() if v > 1])


def main():
    l = [1, 2, 3, 1, 1, 3]
    ans = Solution().numIdenticalPairs(l)
    print(ans)


if __name__ == "__main__":
    main()
