arr = []

with open("problem12.txt") as f:
    arr = f.read().splitlines()


ans = 0
ans2 = 0
rowSize = len(arr)
colSize = len(arr[0])
field = {}
for i in range(rowSize):
    for j in range(colSize):
        field[(i,j)] = arr[i][j]
for i in range(rowSize):
    for j in range(colSize):
        crop = field[(i,j)]
        if crop != ".":
            perimeter = 0
            sideCount = 0
            sides = set()
            area = 0
            seen = set([(i,j)])
            queue = [(i,j)]
            field[(i,j)] = '.'
            while queue:
                curI,curJ = queue.pop(0)
                area += 1        
                for x,y in [(1,0),(-1,0),(0,1),(0,-1)]:
                    newPos = (curI+x,curJ+y)
                    if newPos in field and crop == field[newPos]:
                        queue.append((newPos))
                        field[(newPos)] = '.'
                        seen.add((newPos))
                    else:
                        if not newPos in field or not newPos in seen:
                            perimeter += 1   
                            if x == 1:
                                sides.add(("DOWN",newPos))
                            elif x == -1:
                                sides.add(("UP",newPos))
                            elif y == 1:
                                sides.add(("RIGHT",newPos))
                            elif y == -1:
                                sides.add(("LEFT",newPos))
                            
            while sides:
                direc,pos = sides.pop()
                if direc == "DOWN" or direc == "UP":
                    left = pos[1] - 1
                    while (direc,(pos[0],left)) in sides:
                        sides.remove((direc,(pos[0],left)))
                        left -= 1
                    right = pos[1] + 1
                    while (direc,(pos[0],right)) in sides:
                        sides.remove((direc,(pos[0],right)))
                        right += 1
                if direc == "RIGHT" or direc == "LEFT":
                    up = pos[0] - 1
                    while (direc,(up,pos[1])) in sides:
                        sides.remove((direc,(up,pos[1])))
                        up -= 1
                    down = pos[0] + 1
                    while (direc,(down,pos[1])) in sides:
                        sides.remove((direc,(down,pos[1])))
                        down += 1
                sideCount += 1
 



            ans += perimeter * area
            ans2 += sideCount * area
print(ans)
print(ans2)






