def ArrayChallenge(strArr: list[str]):
    # code goes here
    # need to find the target nodes
    arr = strArr[0][1:-1].replace(" ", "").split(",")
    ans = arr[0]
    if len(arr) < 4:
        # only root is parent
        return ans
    t1 = strArr[1]
    t2 = strArr[2]
    t1parents: list[str] = []
    t2parents: list[str] = []

    def _rec(i: int, parents: list[str]):
        # submitted answer don't include this check
        if arr[i] == "#":
            return

        if arr[i] == t1:
            t1parents.extend(parents)
        elif arr[i] == t2:
            t2parents.extend(parents)
        left = 2 * i + 1
        right = 2 * i + 2
        if left < len(arr):
            _rec(left, parents + [arr[i]])
        if right < len(arr):
            _rec(right, parents + [arr[i]])

    # traverse array
    _rec(0, [])
    print(t1parents)
    print(t2parents)

    if t1 in t2parents:
        return t1
    if t2 in t1parents:
        return t2
    # need to catch if 1 of the target is the parent of the other
    # shortest+1 will be 1 of the target if the other target is its descendant
    # lca is the index before the parent node diverge
    if len(t1parents) < len(t2parents):
        if t2parents[len(t1parents)] == t1:
            return t1
        shortest = len(t1parents)

    elif len(t1parents) > len(t2parents):
        shortest = len(t2parents)
        if t1parents[len(t2parents)] == t2:
            return t2
    else:
        shortest = len(t1parents)

    for i in range(shortest):
        if t1parents[i] == t2parents[i]:
            ans = t1parents[i]
        else:
            break
    return ans


if __name__ == "__main__":
    arr = ["[12, 5, 9, 6, 2, 0, 8, #, #, 7, 4, #, #, #, #]", "6", "4"]
    ans = ArrayChallenge(arr)
    print(ans)  # 5
    arr = ["[12, 5, 9, 6, 2, 0, 8, #, #, 7, 4, #, #, #, #]", "6", "0"]
    ans = ArrayChallenge(arr)
    print(ans)  # 12
    arr = ["[5, 2, 6, 1, #, 8, #]", "2", "6"]
    ans = ArrayChallenge(arr)
    print(ans)  # 5
    arr = ["[5, 2, 6, 1, #, 8, 12, #, #, #, #, #, #, 3, #]", "3", "12"]
    ans = ArrayChallenge(arr)
    print(ans)  # 12
