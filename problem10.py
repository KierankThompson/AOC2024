arr = []
with open("problem10.txt") as f:
    arr = f.read().splitlines()
rowSize = len(arr)
colSize = len(arr[0])
ans = 0
ans2 = 0
for i,row in enumerate(arr):
    for j,num in enumerate(row):
        seen = set()
        if num == "0":
            queue = [(0,i,j)]
            while queue:
                curNum,curI,curJ = queue.pop()
                if curNum == 9:
                    seen.add((curI,curJ))
                    ans2 += 1
                else:
                    for x,y in [(0,1),(0,-1),(1,0),(-1,0)]:
                        if 0 <= curI + x < rowSize and 0 <= curJ + y < colSize and int(arr[curI+x][curJ+y]) == curNum+1:
                            queue.append((curNum+1,curI+x,curJ+y))
        ans += len(seen)
print(ans)
print(ans2)
