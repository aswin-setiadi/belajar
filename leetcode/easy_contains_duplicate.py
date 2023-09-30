#!/bin/python3
# https://leetcode.com/problems/contains-duplicate/
class Solution:
    # beat 34.55% speed, 13.13% memory
    def containsDuplicate(self, nums: list[int]) -> bool:
        results = {}
        for item in nums:
            if item in results:
                return True
            else:
                results[item] = 1
        return False

    # 77.82% 88.17%
    def containsDuplicateSet(self, nums: list[int]) -> bool:
        results: set[int] = set()
        for item in nums:
            if item in results:
                return True
            else:
                results.add(item)
        return False

    # 5% 98.55%
    def containsDuplicate2(self, nums: list[int]) -> bool:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False

    def containsDuplicate3(self, nums: list[int], depth: int = 0) -> bool | list[int]:
        if len(nums) > 2:
            sub1 = self.containsDuplicate3(
                [nums[i] for i in range(len(nums) // 2)], depth + 1
            )
            sub2 = self.containsDuplicate3(
                [nums[i] for i in range(len(nums) // 2, len(nums))], depth + 1
            )
            if (sub1 is True) or (sub2 is True):
                return True
            else:
                arr = [0] * (len(sub1) + len(sub2))
                ptr1 = ptr2 = 0
                while not (ptr1 == len(sub1) or ptr2 == len(sub2)):
                    if sub1[ptr1] < sub2[ptr2]:
                        arr[ptr1 + ptr2] = sub1[ptr1]
                        ptr1 += 1
                    elif sub1[ptr1] > sub2[ptr2]:
                        arr[ptr1 + ptr2] = sub2[ptr2]
                        ptr2 += 1
                    else:
                        return True
                if ptr1 != len(sub1):
                    for i in range(ptr1, len(sub1)):
                        arr[i + ptr2] = sub1[i]
                elif ptr2 != len(sub2):
                    for i in range(ptr2, len(sub2)):
                        arr[i + ptr1] = sub2[i]
                if depth == 0:
                    return False
                else:
                    return arr
        elif len(nums) == 2:
            if nums[0] != nums[1]:
                if depth == 0:
                    return False
                else:
                    return nums if nums[0] < nums[1] else [nums[1], nums[0]]
            else:
                return True
        else:
            if depth == 0:
                return False
            else:
                return nums


if __name__ == "__main__":
    l = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]
    ans = Solution().containsDuplicate3(l)
    print(ans)
