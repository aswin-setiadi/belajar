class Solution:
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
    # wip
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
            return prev_total
        current_total = self.arr[index] + prev_total
        if current_total == self.target:
            return current_total
        if current_total < self.target:
            tmp1 = self._solve_util(index + 1, prev_total)
            tmp2 = self._solve_util(index + 1, current_total)
            return max(tmp1, tmp2)


def main():
    ans = Solution([1, 2, 3, 9], 8).solve()
    print(ans)
    ans = Solution([1, 2, 4, 4], 8).solve()
    print(ans)


if __name__ == "__main__":
    main()
