#!/bin/python3

import math
import os
import random
import re
import sys
from typing import List, Tuple

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#
from operator import abs, sub


# code by discussion in hackerrank
def formingMagicSquare(s: List[int] = [5, 3, 4, 1, 5, 8, 6, 4, 2]):
    # Write your code here

    squares = (
        [
            5 + a,
            5 - (a + b),
            5 + b,
            5 - (a - b),
            5,
            5 + (a - b),
            5 - b,
            5 + (a + b),
            5 - a,
        ]
        for a, b in [
            (1, 3),
            (3, 1),
            (1, -3),
            (3, -1),
            (-1, 3),
            (-3, 1),
            (-1, -3),
            (-3, -1),
        ]
    )

    return min(sum(map(abs, map(sub, square, s))) for square in squares)


def generate_magics(n=3):
    def _generate_rotates(ms, m, count):
        if not count:
            return
        else:
            rotated = [[] for _ in range(n)]
            for v1 in m:
                for k2, v2 in enumerate(v1[::-1]):
                    rotated[k2].append(v2)
            ms.append(rotated)
            _generate_rotates(ms, rotated, count - 1)

    a = [[8, 3, 4], [1, 5, 9], [6, 7, 2]]
    magics = [a]
    _generate_rotates(magics, a, 3)

    a_t = [[] for _ in range(n)]
    for k1, v1 in enumerate(a):
        for k2, v2 in enumerate(v1):
            a_t[k2].append(v2)
    magics.append(a_t)
    _generate_rotates(magics, a_t, 3)
    return magics


class Solution:
    magic_squares = generate_magics()

    def __init__(self) -> None:
        pass

    @classmethod
    def solve(cls, s=[[5, 3, 4], [1, 5, 8], [6, 4, 2]]):
        min_cost = math.inf
        for magic_square in Solution.magic_squares:
            cost = 0
            for k1, v1 in enumerate(magic_square):
                for k2, v2 in enumerate(v1):
                    cost += abs(s[k1][k2] - v2)
            min_cost = min(min_cost, cost)
        print(min_cost)
        return min_cost


if __name__ == "__main__":
    # os.environ["OUTPUT_PATH"] = "triplet.txt"
    # fptr = open(os.environ["OUTPUT_PATH"], "w")

    # s = []

    # for _ in range(3):
    #     s.append(list(map(int, input().rstrip().split())))

    # result = formingMagicSquare(s)

    # fptr.write(str(result) + "\n")

    # fptr.close()
    # print(formingMagicSquare())
    Solution().solve()
