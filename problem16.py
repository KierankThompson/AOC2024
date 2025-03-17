map = set()
rowSize = 0 
colSize = 0
with open("problem16.txt") as f:
    arr = f.read().splitlines()
    rowSize = len(arr)
    colSize = len(arr[0])
    for i,line in enumerate(arr):
        for j,ch in enumerate(line):
            if ch == ".":
                map.add((i,j))

start = (rowSize-2,1)
map.add(start)        
goal = (1,colSize-2)
map.add(goal)
path = {start:0}
spots =  set()
bestScore = 1e9
queue = [(start,(0,1),[start])]
dirDic = {(0,1):[(0,1),(1,0),(-1,0)],(1,0):[(1,0),(0,1),(0,-1)],(-1,0):[(-1,0),(0,1),(0,-1)],(0,-1):[(0,-1),(1,0),(-1,0)]}
while queue:
    cur, direction,arr = queue.pop(0)
    if cur == goal:
        if path[goal] < bestScore:
            spots = arr
            bestScore = path[goal]
        elif path[goal] == bestScore:
            spots += arr
    for posD in dirDic[direction]:
        newPos = (cur[0] + posD[0], cur[1] + posD[1])
        if newPos not in map:
            continue
        newScore = path[cur]
        newScore += 1 if direction == posD else 1001
        if newPos not in path or path[newPos] >= newScore:
            path[newPos] = newScore
            queue.append((newPos,posD,arr+[newPos]))
print(path[goal])
print(len(set(spots)))
"""
arr = [["." if (i,j) in path else "#" for i in range(colSize)] for j in range(rowSize)]
for s in spots:
    arr[s[0]][s[1]] = "!"
with open("output.txt","w") as f:
    for line in arr:
        f.write("".join(line)+"\n")
"""
     












