#!/bin/python3


class Solution:
    """
    quicksort have pivot normally at last element, steps:
    i from 0, pivot is last element, j from last-1
    i iterate to right until i>pivot found, then j iterate to left until j <44, if found swap item i with j, then i continue again
    if j position <= i, done since left of i are smaller than pivot, swap i with pivot, if i on pivot, nothing to swap

    then recursively sort left and right

    in case i and j start at same index, i can traverse to pivot if item at i < p
    """

    @staticmethod
    def partition(arr: list[int], left: int, right: int):
        i = left
        j = right - 1
        p = arr[right]
        while i < j:
            while i < right and arr[i] < p:
                i += 1

            while j > left and arr[j] >= p:
                j -= 1

            if i < j:
                # element i bigger than j, so swap
                arr[i], arr[j] = arr[j], arr[i]
        # i and j cursor pass each other
        if arr[i] > p:
            arr[i], arr[right] = arr[right], arr[i]

        return i

    @staticmethod
    def solve(arr: list[int], left: int, right: int):
        if left < right:
            partition_pos = Solution.partition(arr, left, right)
            Solution.solve(arr, left, partition_pos - 1)
            Solution.solve(arr, partition_pos + 1, right)


arr = [22, 11, 88, 66, 55, 77, 33, 44]
Solution.solve(arr, 0, len(arr) - 1)
print(arr)
