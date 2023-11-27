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
    @staticmethod
    def solve(arr: list[list[int]], target_cell: tuple[int, int]) -> int:
        """
        Find shortest path (with weight) to target cell, brute force (check all possible set of path)
        There is weight, so can't use memoization cause it will need to compare all possible weight set
        This is bottom up approach cause start from end cell

        """

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

        return _rec_util(target_cell[0], target_cell[1], 0)


class Solution3:
    """
    still brute force finding shortest path (with weight) top down approach
    """

    def __init__(self, matrix: list[list[int]], target_cell: tuple[int, int]) -> None:
        self.matrix = matrix
        self.target_cell = target_cell
        self.maxrowindex = len(matrix) - 1
        self.maxcolindex = len(matrix[0]) - 1
        self.ans = [[[-1] for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
        self.smallest_cost = sys.maxsize

    def solve(self, row: int, col: int, cost: int):
        if row == self.target_cell[0] and col == self.target_cell[1]:
            self.smallest_cost = min(self.smallest_cost, cost + self.matrix[row][col])
        if row < self.maxrowindex:
            self.solve(row + 1, col, cost + self.matrix[row][col])
        if col < self.maxcolindex:
            self.solve(row, col + 1, cost + self.matrix[row][col])


class Knapsack:
    """colin galen extra problem 2 knapsack"""

    @staticmethod
    def solve(arr: list[int], total: int):
        last = len(arr) - 1

        def _rec(index: int, total_left: int) -> bool:
            if arr[index] == total_left:
                return True
            if index == last:
                return False
            else:
                if arr[index] > total_left:
                    return _rec(index + 1, total_left)
                else:
                    return _rec(index + 1, total_left - arr[index])

        return _rec(0, total)


def main1():
    ans = Solution1.solve_rec(3, 3, (2, 2))
    print(ans)
    ans2 = Solution1.solve_iter(3, 3, (2, 2))
    print(ans2)


def main2():
    matrix: list[list[int]] = [[4, 9, 7, 2], [3, 8, 5, 2], [1, 2, 6, 4], [4, 3, 2, 2]]
    for row in matrix:
        print(row)
    ans2 = Solution2.solve(matrix, (3, 3))
    print(ans2)
    ans3 = Solution3(matrix, (3, 3))
    ans3.solve(0, 0, 0)
    print(ans3.smallest_cost)


def main3():
    arr = [3, 5, 2, 7, 9]
    t = 10
    print(Knapsack.solve(arr, t))  # True
    arr = [2, 4, 6]
    t = 11
    print(Knapsack.solve(arr, t))  # False
    arr = [2, 7, 3, 4, 9, 5, 6, 1, 8]
    t = 25
    print(Knapsack.solve(arr, t))  # True


if __name__ == "__main__":
    # main1()
    # main2()
    main3()
