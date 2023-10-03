# Find My Number

## Assumptions

1. Keypad layout is fixed.

## Runtime

First successful run using time.time_ns()

- naive dfs= 801.8434047698975 ms
- replace seq ```list[str]``` to depth ```int```= 228.40213775634766 ms
- use memoization to keep track of traversed path= 9.593500 ms

Using time.perf_counter()

- naive dfs= 3.387205 ms
- replace seq ```list[str]``` to depth ```int```= 1.746320 ms
- use memoization to keep track of traversed path= 0.002575 ms