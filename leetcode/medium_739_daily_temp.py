def dt(tmp):
    #leetcode answer
    res=[0]* len(tmp)
    stack=[]
    for i,t in enumerate(tmp):
        while stack and t> stack[-1][0]:
            stackT, stackInd= stack.pop()
            res[stackInd]=i-stackInd
        stack.append((t,i))
    return res

print(dt([30,38,30,36,35,40,28]))