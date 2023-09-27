#!/bin/python3

# https://www.hackerrank.com/challenges/mini-max-sum/problem

from typing import List

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def miniMaxSum(arr: List[int]):
    # Write your code here
    if arr[0] <= arr[1]:
        min = arr[0]
        max = arr[1]
    else:
        min = arr[1]
        max = arr[0]
    for i in arr[2:5]:
        if i < min:
            min = i
        if i > max:
            max = i
    total = sum(arr)
    print(f"{total-max} {total-min}")


if __name__ == "__main__":
    # arr = list(map(int, input().rstrip().split()))
    arrs = [
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [1, 1, 1, 1, 1],
        [1, 2, 2, 3, 4],
        [23, 31, 10, 1, 23],
    ]
    for arr in arrs[:]:
        miniMaxSum(arr)
