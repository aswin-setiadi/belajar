#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#


def birthdayCakeCandles(candles):
    # Write your code here
    tallest = 0
    count = 0
    for c in candles:
        if c > tallest:
            tallest = c
            count = 1
        elif c == tallest:
            count += 1
    print(f"tallest candle={tallest} count={count}")
    return count


if __name__ == "__main__":
    os.environ["OUTPUT_PATH"] = "candle.txt"
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + "\n")

    fptr.close()
