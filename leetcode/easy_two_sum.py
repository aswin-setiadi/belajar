#!/bin/python3
# https://leetcode.com/problems/two-sum/description/


class Solution:
    def twoSum(self, nums: list[int], target: int):
        """
        bigO n^2, 36.64% 97.44%
        """
        remainders: list[int] = []
        for k, v in enumerate(nums):
            r = target - nums[k]
            for i, j in enumerate(remainders):
                if r == j:
                    return [i, k]
            remainders.append(v)

    def twoSumDict(self, nums: list[int], target: int):
        """
        bigO n, 48.37% 28.05%
        """
        remainders: dict[int, int] = {}
        for k, v in enumerate(nums):
            r = target - v
            if r in remainders:
                return [remainders[r], k]
            remainders[v] = k


if __name__ == "__main__":
    l = [[2, 7, 11, 15, 9], [3, 2, 4, 6], [3, 3, 6], [1, 2, 3, 6]]
    for _ in l:
        ans = Solution().twoSumDict(_[:-1], _[-1])
        print(ans)
