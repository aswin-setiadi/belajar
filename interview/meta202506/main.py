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
    midDistance=((abs(maxValue)+abs(minValue))/2)
    if midDistance%1!=0:
        return False
    else:
        midLocation=minValue+midDistance
        seen=[]
        for k in sorted(d):
            if k in seen:
                continue
            else:
                if k<midLocation:
                    k_mirror=midLocation+(midLocation-k)
                    if k_mirror in d:
                        if len(d[k])!=len(d[k_mirror]):
                            return False
                        else:
                            if set(d[k])!=set(d[k_mirror]):
                                return False
                            else:
                                seen.append(k_mirror)
                    else:
                        return False
                else:
                    return False
        return midLocation

def main1():
    print(shorten_word(""))
    print(shorten_word("a"))
    print(shorten_word("ab"))
    print(shorten_word("abc"))

def main2():
    print(symmetrical_seperation(((0,0), (0,1))))
    print(symmetrical_seperation(((-2,0), (0,0))))
    print(symmetrical_seperation(((-2,4), (-1,2), (2,4), (1,2))))

if __name__=="__main__":
    main1()
    main2()