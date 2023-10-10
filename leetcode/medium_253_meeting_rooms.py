from itertools import accumulate

ints = [[0, 30], [5, 10], [15, 20]]

points = sorted([(i, 1) for i, _ in ints] + [(j, -1) for _, j in ints])
print(points)
print("ans=", end=" ")
print(max(accumulate(j for _, j in points)))
