class Solution:
    """
    The window keep track of the longest valid ones so far
    It will keep sliding until l meet 0, then it will allow to widen the window to update the max ans if r is 1
    """

    def longestOnes(self, nums: list[int], k: int) -> int:
        l = r = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                k -= 1
            if k < 0:
                if nums[l] == 0:
                    k += 1
                l += 1
        return r - l + 1


def main():
    # 0 3 6, len=10
    arr = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1]
    arr2 = [1, 1, 0, 1, 0, 1, 0, 1, 1, 1]
    k = 2
    ans = Solution().longestOnes(arr, k)
    ans2 = Solution().longestOnes(arr2, k)
    print(ans)
    print(ans2)


if __name__ == "__main__":
    main()
