from math import ceil
from typing import List


class Solution:
    def minDayskVariants(self, points: List[List[int]], k: int) -> int:
        min_x = min(x[0] for x in points)
        min_y = min(x[1] for x in points)
        max_x = max(x[0] for x in points)
        max_y = max(x[1] for x in points)

        min_days = max(max_x, max_y) + 1

        for i in range(min_x, max_x + 1):
            for j in range(min_y, max_y + 1):
                d = []
                for p in points:
                    dist = abs(p[0] - i) + abs(p[1] - j)
                    d.append(dist)
                d.sort()
                min_days = min(min_days, d[k - 1])
        return min_days


if __name__ == "__main__":
    points = [[3, 3], [1, 2], [9, 2]]
    k = 3
    mindays = Solution().minDayskVariants(points, k)
    print(mindays)
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
