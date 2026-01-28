
# 10 20 20 30 40 40
# 1  2  2  3  4  4
# 0  1  2  3  4  5
def main1(l:list[int]):
    if len(l)<2:
        return l
    l_sorted= sorted(l)
    d={}
    rank=1
    for i in range(len(l_sorted)):
        if l_sorted[i] not in d:
            d[l_sorted[i]]= rank
            rank+=1
    return [d[x] for x in l]

# foo,10,b
# foo,20,e
# foo,25,b
# bar,30,b
# bar,40,e
# foo,50,e

# foo=10,5+10
# bar=10

def main2a(ls):
    stack=[]
    res={}
    for i in range(len(ls)):
        if ls[i][2]=="b":
            if ls[i][0] not in res:
                res[ls[i][0]]=0
            stack.append(ls[i])
        elif ls[i][2]=="e":
            top_s=stack[-1]
            if top_s[0]==la[i][0]:
                res[ls[i][0]]+=ls[i][1]-top_s[1]
                last_exit_time=top_s[1]

def main2b(ls):
    res={ls[0][0]:0}
    for i in range(1,len(ls)):
        if ls[i][2]=="b":
            if ls[i][0] not in res:
                res[ls[i][0]]=0
            if ls[i-1][2]=="b":
                res[ls[i-1][0]]+=(ls[i][1]-ls[i-1][1])
        elif ls[i][2]=="e":
            res[ls[i][0]]+=(ls[i][1]-ls[i-1][1])
    return res

def main2c(l):
    res={}
    prev=l[0]
    res[prev[0]]=0
    for x in l[1:]:
        t= x[1]-prev[1]
        if x[2]=="b":
            if x[0] not in res:
                res[x[0]]=0
            if prev[2]=="b":
                res[prev[0]]+=t
            # else:
            #     res[x[0]]+=t
        else:
            res[x[0]]+=t
        prev=x
    return res

if __name__=="__main__":
    print(main1([100,20,10,50,10,40,90,90]))
    print(main2c([
        ["foo",10,"b"],
        ["foo",20,"e"],
        ["foo",25,"b"],
        ["bar",30,"b"],
        ["bar",40,"e"],
        ["foo",50,"e"],
    ]))
