#!/bin/python3
# from https://stackoverflow.com/a/31453147/3728943
import operator


class Solution:
    @staticmethod
    def merge(l: list[int], r: list[int], compare) -> list[int]:
        result: list[int] = []
        i, j = 0, 0
        while i < len(l) and j < len(r):
            if compare(l[i], r[j]):
                result.append(l[i])
                i += 1
            else:
                result.append(r[j])
                j += 1
        while i < len(l):
            result.append(l[i])
            i += 1
        while j < len(r):
            result.append(r[j])
            j += 1
        return result

    @staticmethod
    def solve(nums: list[int], compare=operator.lt):
        if len(nums) < 2:
            return nums
        pivot = len(nums) // 2
        left = Solution.solve(nums[:pivot], compare)
        right = Solution.solve(nums[pivot:], compare)
        return Solution.merge(left, right, compare)


if __name__ == "__main__":
    qns = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [5, 0, 4, 1, 3, 2]]
    for qn in qns:
        ans = Solution.solve(qn)
        print(ans)
