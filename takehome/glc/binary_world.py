class Solution:
    WORLD_TYPES={"0":"binary","1":"decimal"}
    @classmethod
    def main(cls):
        _= input().split()
        _=[int(x) for x in _]
        cls.H=_[0]
        cls.W=_[1]
        cls.WORLD=[]
        for i in range(cls.H):
            _=input()
            cls.WORLD.append(list(_))
        test_count=int(input())
        cls.TESTS=[]
        for i in range(test_count):
            _=input()
            _= [int(x)-1 for x in _]
            cls.TESTS.append([(_[0],_[1]),(_[2],_[3])])
        for t in cls.TESTS:
            cls.FOUND=[False]
            cls.solve(t)
            if not cls.FOUND[0]:
                print("neither")

    @classmethod
    def solve(cls, coords:list[tuple]):
        start:tuple[int,int] = coords[0]
        target:tuple[int,int] = coords[1]
        if cls.WORLD[start[0]][start[1]]!=cls.WORLD[target[0]][target[1]]:
            return
        else:
            cls.MEMORY=[[0 for x in range(cls.W)] for y in range(cls.H)]
            cls.traverse(start,target)

    @classmethod
    def test_run(cls):
        cls.H=10
        cls.W=20
        # cls.H=1
        # cls.W=4
        tmp="""11111111111111111111
        11000000000000000101
        11111111111111110000
        11111111111111110000
        11000000000000000111
        00011111111111111111
        00111111111111111111
        10000000000000001111
        11111111111111111111
        11111111111111111111""".split("\n")
        # tmp=["1100"]
        # tmp=["1111"]
        cls.WORLD=[]
        for row in tmp:
            x=row.strip()
            cls.WORLD.append(list(x))
        cls.TESTS=[[(1,2),(7,15)],[(7,0),(6,2)],[(0,0),(9,19)]]
        # cls.TESTS=[[(0,0),(0,3)],[(0,0),(0,0)]]
        # cls.TESTS=[[(0,0),(0,2)]]
        for t in cls.TESTS:
            cls.FOUND=[False]
            cls.solve(t)
            if not cls.FOUND[0]:
                print("neither")


    @classmethod
    def traverse(cls, start:tuple[int,int], target:tuple[int,int]):
        if start==target:
            print(cls.WORLD_TYPES[cls.WORLD[start[0]][start[1]]])
            cls.FOUND[0]=True
        elif cls.FOUND[0]:
            return
        elif cls.MEMORY[start[0]][start[1]]!=1:
            land_type=cls.WORLD[start[0]][start[1]]
            cls.MEMORY[start[0]][start[1]]=1
            if start[0]-1>=0 and cls.WORLD[start[0]-1][start[1]]==land_type:
                cls.traverse((start[0]-1, start[1]),target)
            if start[0]+1<cls.H and cls.WORLD[start[0]+1][start[1]]==land_type:
                cls.traverse((start[0]+1, start[1]),target)
            if start[1]-1>=0 and cls.WORLD[start[0]][start[1]-1]==land_type:
                cls.traverse((start[0], start[1]-1),target)
            if start[1]+1<cls.W and cls.WORLD[start[0]][start[1]+1]==land_type:
                cls.traverse((start[0], start[1]+1),target)

if __name__=="__main__":
    Solution.main()
