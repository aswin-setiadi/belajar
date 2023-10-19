import math
from typing import List


def search_rotated_sorted_distinct_array(nums: List[int], target: int) -> int:
    # sorted means start < pivot < end
    # e.g. 0,1,2,_3,4,5,6 | 1,2,3,_4,5,6,0 | 2,3,4,_5,6,0,1 | 3,4,5,_6,0,1,2 | 4,5,6,_0,1,2,3 | 5,6,0,_1,2,3,4 | 6,0,1,_2,3,4,5
    def _search(start: int, end: int) -> int:
        p = start + math.floor((end - start) / 2)
        # \print(f"s={start} e={end} p={p}")
        # input("pause")
        if nums[p] == target:
            return p
        if target < nums[p]:
            return _search(start, p - 1)
        else:
            return _search(p + 1, end)

    def _search_rotated(s: int, e: int) -> int:
        if s == e:
            if nums[s] == target:
                return s
            else:
                return -1
        p = s + math.floor((e - s) / 2)
        # print(f"s={s} e={e} pivot={p}")
        if nums[p] == target:
            return p
        if nums[p] > nums[s]:
            # left is sorted
            if target < nums[p]:
                if target >= nums[s]:
                    if p == s:
                        return _search_rotated(s, p)
                    else:
                        return _search_rotated(s, p - 1)
            #     else:
            #         return _search_rotated(p+1,e)
            # else:
            return _search_rotated(p + 1, e)
        else:
            # right is sorted
            if target > nums[p]:
                if target <= nums[e]:
                    return _search_rotated(p + 1, e)
            #     else:
            #         return _search_rotated(s,p-1)
            # else:
            if p == s:
                return _search_rotated(s, p)
            else:
                return _search_rotated(s, p - 1)

    start = 0
    end = len(nums) - 1
    pivot = math.floor(len(nums) / 2)
    # print(f"pivot={pivot}")
    if nums[pivot] == target:
        # handle len=1 case
        return pivot

    if nums[start] < nums[end]:
        # ori order
        if target < nums[pivot]:
            return _search(start, pivot - 1)
        return _search(pivot + 1, end)
    else:
        # rotated
        return _search_rotated(start, end)


# leetcode answer
class Solution:
    def search(self, nums: list[int], target: int):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (r - l) // 2
            if nums[mid] == target:
                return mid
            if nums[l] < nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1


if __name__ == "__main__":
    n = list(range(7))
    # print(n)
    # for i in range(7):
    #     answer=search_rotated_sorted_distinct_array(n,n[i])
    #     print(f"answer={answer}")
    # print("rotated:")
    # #rotate 6 times
    # for i in range(6):
    #     m= 2*n
    #     m= m[i+1:len(n)+i+1]
    #     print(m)
    #     for i in range(7):
    #         answer=search_rotated_sorted_distinct_array(m,m[i])
    #         print(f"target={m[i]} answer={answer}")

    #     answer=search_rotated_sorted_distinct_array(m,10)
    #     input(answer)
    nums = [4, 5, 6, 7, 0, 1, 2]
    ans = search_rotated_sorted_distinct_array(nums.copy(), 0)
    ans2 = Solution().search(nums.copy(), 0)
    print(ans)
    print(ans2)
