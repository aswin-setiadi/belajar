def shorten_word(s: str):
    """internationalisation can be shortened to i18n. Write a function to check if a word can be shortened to a pattern"""
    if len(s) < 2:
        return s
    else:
        return f"{s[0]}{len(s)-2}{s[-1]}"


def symmetrical_seperation(points: tuple[tuple[int, int]]):
    "given a bunch of (x, y) points on a Cartesian graph, write a function to check if any vertical line can symmetrically separate the points"
    if len(points)<1:
        return False
    d={}
    maxValue= float("-inf")
    minValue= float("inf")
    for t in points:
        if t[0] not in d:
            d[t[0]]={t[1]}
        else:
            d[t[0]].add(t[1])
        maxValue=max(t[0],maxValue)
        minValue=min(t[0], minValue)
    if maxValue==minValue:
        return maxValue
    midValue=((abs(maxValue)+abs(minValue))/2)
    if midValue%2!=0:
        return False
    else:
        midLocation=minValue+midValue
        for k in sorted(d):
            if k<midLocation and k<midValue
            
            else:
                return False

