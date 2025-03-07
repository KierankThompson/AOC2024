import time
tiles = {}
curX = 0
curY = 0
rowSize = 0
colSize = 0
dirChange = {"^":">",">":"v","v":"<","<":"^"}
dirAdd = {"^":(-1,0),">":(0,1),"v":(1,0),"<":(0,-1)}
with open("problem6.txt") as f:
    lines = f.read().splitlines()
    rowSize = len(lines)
    colSize = len(lines[0])
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == '^':
                curX = i
                curY = j
                tiles[(i,j)] = "."
            else:
                tiles[(i,j)] = lines[i][j]
curDir = "^"
visited = set()
oX = curX
oY = curY
while curX < rowSize and curX >= 0 and curY < colSize and curY >= 0:
    if tiles[(curX,curY)] != "#":
        visited.add((curX,curY))
    else:
        curX -= dirAdd[curDir][0]
        curY -= dirAdd[curDir][1]
        curDir = dirChange[curDir]
    curX += dirAdd[curDir][0]
    curY += dirAdd[curDir][1]
print(len(visited))


numBlocks = 0
start = time.time()
for tile in visited:
    curX = oX
    curY = oY
    tiles[tile] = "#"
    curDir = "^"
    visited2 = set()
    while curX < rowSize and curX >= 0 and curY < colSize and curY >= 0:
        if (curX,curY,curDir) in visited2:
            numBlocks += 1
            break
        if tiles[(curX,curY)] != "#":
            visited2.add((curX,curY,curDir))
        else:
            curX -= dirAdd[curDir][0]
            curY -= dirAdd[curDir][1]
            curDir = dirChange[curDir]
        curX += dirAdd[curDir][0]
        curY += dirAdd[curDir][1]
    tiles[tile] = "."
end = time.time()
print(numBlocks)
