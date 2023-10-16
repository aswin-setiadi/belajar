class Solution:
    def rotate(self, nums: list[int], k: int) -> list[int]:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1 or k == 0:
            return nums
        k = k % len(nums)
        nums = nums[-k:] + nums[: k + 1]
        return nums


def main():
    ans = Solution().rotate([1, 2, 3, 4, 5, 6, 7], 3)
    print(ans)


if __name__ == "__main__":
    main()
