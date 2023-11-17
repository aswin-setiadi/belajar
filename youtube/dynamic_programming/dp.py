#!/bin/python3
# https://www.youtube.com/watch?v=Clp5c7HvLqs
import sys


class Solution1:
    """
    question about minimum distance (no weight) to goal cell
    """

    @staticmethod
    def solve_rec(m: int, n: int, end_cell: tuple[int, int]) -> int:
        """
        recursive from goal cell back to original cell
        """

        ans: list[list[int]] = [[-1 for _ in range(n)] for _ in range(m)]
        end_x = end_cell[0]
        end_y = end_cell[1]

        def _solve_util(row: int, col: int) -> int:
            if row == 0 and col == 0:
                return 1
            if ans[row][col] != -1:
                return ans[row][col]
            step_count: int = 0
            if row > 0:
                step_count += _solve_util(row - 1, col)
            if col > 0:
                step_count += _solve_util(row, col - 1)

            ans[row][col] = step_count
            return step_count

        return _solve_util(end_x, end_y)

    @staticmethod
    def solve_iter(m: int, n: int, end_cell: tuple[int, int]) -> int:
        ans: list[list[int]] = [[0 for _ in range(n)] for _ in range(m)]
        ans[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i + 1 < m:
                    ans[i + 1][j] += ans[i][j]
                if j + 1 < n:
                    ans[i][j + 1] += ans[i][j]

        return ans[m - 1][n - 1]


class Solution2:
    """
    Find shortest path to target cell brute force (check all possible set of path)
    """

    @staticmethod
    def solve(arr: list[list[int]], target_cell: tuple[int, int]) -> int:
        m = len(arr)
        n = len(arr[0])

        def _rec_util(row: int, col: int, cost: int) -> int:
            cur_cost: int = arr[row][col] + cost
            # only possible left or top
            if row == 0 and col == 0:
                return cur_cost
            if row > 0:
                fromtop = _rec_util(row - 1, col, cur_cost)
            else:
                fromtop = sys.maxsize
            if col > 0:
                fromleft = _rec_util(row, col - 1, cur_cost)
            else:
                fromleft = sys.maxsize
            return min(fromtop, fromleft)

        return _rec_util(m - 1, n - 1, 0)


def main1():
    ans = Solution1.solve_rec(3, 3, (2, 2))
    print(ans)
    ans2 = Solution1.solve_iter(3, 3, (2, 2))
    print(ans2)


def main2():
    matrix: list[list[int]] = [[4, 9, 7], [3, 8, 5], [1, 2, 6]]
    ans = Solution2.solve(matrix, (2, 2))
    print(ans)


if __name__ == "__main__":
    # main1()
    main2()
