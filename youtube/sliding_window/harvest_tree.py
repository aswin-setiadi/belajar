#!/bin/python3

# above shebang means use the interpreter /bin/python3 in the path env var

from typing import List, Tuple

# https://www.youtube.com/watch?v=ubOhA56G_tk 6:21

# fruits[i] represent the type of fruit tree i is
# given 2 basket, find the starting tree where you can get max total fruit
# [a, o, b, o] start from i=1


class Solution:
    def __init__(self) -> None:
        pass

    @classmethod
    def solve(cls, arr: List[str]) -> Tuple[int, int]:
        if len(arr) < 3:
            return len(arr), 0

        # at least 3 trees exist
        fruits_count = 1
        fruit_types = [arr[0]]
        start1 = 0
        start2 = 0

        for i, v in enumerate(arr[1:], 1):
            fruits_count += 1
            if v != fruit_types[0]:
                fruit_types.append(v)
                start2 = i
                break
        # if a,a,b caught here
        if fruits_count == len(arr):
            return fruits_count, 0

        max_fruits = fruits_count
        final_start = start1
        for i, v in enumerate(arr[max_fruits:], max_fruits):
            if v in fruit_types:
                fruits_count += 1
                if v != arr[start2]:
                    start2 = i
            else:
                # found 3rd fruit_type for this segment
                if fruits_count > max_fruits:
                    max_fruits = fruits_count
                    final_start = start1
                start1 = start2
                start2 = i
                fruit_types = [arr[start1], arr[start2]]
                fruits_count = start2 - start1 + 1

        if fruits_count > max_fruits:
            max_fruits = fruits_count
            final_start = start1
        return max_fruits, final_start


if __name__ == "__main__":
    arr = [
        [],
        ["a"],
        ["a", "b"],
        ["a", "a", "b"],
        ["a", "b", "a"],
        ["a", "b", "c"],
        ["a", "a", "a", "b", "b", "b", "c", "d", "d", "d", "d", "d"],
        ["a", "a", "a", "b", "b", "b", "c", "d", "d", "d", "d", "d", "c"],
        ["a", "o", "b", "o"],
        ["a", "a", "b", "b", "c", "c", "c", "a"],
        ["a", "a", "b", "b", "c", "c", "c", "a", "a", "a"],
    ]
    for a in arr:
        count, index = Solution.solve(a)
        print(
            f"max fruit count={count} start from index={index} items={a[index:index+count]}"
        )
