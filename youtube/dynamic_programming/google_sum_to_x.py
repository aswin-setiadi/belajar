class Solution:
    """
    https://www.youtube.com/watch?v=XKu_SEDAykw
    """

    def __init__(self, arr: list[int], target: int) -> None:
        self.arr = arr
        self.target = target

    def solve_sorted(self):
        l = 0
        r = len(self.arr) - 1

        while l < r:
            cur_sum = self.arr[l] + self.arr[r]
            if cur_sum == self.target:
                return True
            if cur_sum > self.target:
                r -= 1

            elif cur_sum < self.target:
                l += 1

        return False

    def solve(self):
        # check complement
        tmp = self.target - self.arr[0]
        mapping = {tmp: None}
        for item in self.arr[1:]:
            c = self.target - item
            if c in mapping:
                return True
            else:
                mapping[c] = None
        return False


class Solution2:
    # does not work I think cause 2 same element can be considered
    # if only 2 element == target, this solution cant since this algo can consider >2 for total of target
    def __init__(self, arr: list[int], target: int) -> None:
        self.arr = arr
        self.target = target

    def solve(self) -> bool:
        ans = self._solve_util(0, 0)
        if ans == self.target:
            return True
        else:
            return False

    def _solve_util(self, index: int, prev_total: int) -> int:
        if index == len(self.arr):
            return 0
        current_total = self.arr[index] + prev_total
        if current_total == self.target:
            return current_total
        if current_total < self.target:
            tmp1 = self._solve_util(index + 1, prev_total)
            tmp2 = self._solve_util(index + 1, current_total)
            return max(tmp1, tmp2)
        else:
            return 0


def main():
    ls = [
        [1, 2, 3, 9],  # False
        [1, 2, 4, 4],  # True
        [3, 4, 1, 2],  # False
    ]
    for l in ls:
        ans = Solution2(l, 8).solve()
        print(ans)


if __name__ == "__main__":
    main()
