from collections import defaultdict
antinodes = set()
antinodes2 = set()
rowSize = 0
colSize = 0
satellites = defaultdict(list)
with open("problem8.txt") as f:
    lines = f.read().splitlines()
    rowSize = len(lines)
    colSize = len(lines[0])
    for i in range(rowSize):
        for j in range(colSize):
            if lines[i][j] != ".":
                for x,y in satellites[lines[i][j]]:
                    diff = (i-x,j-y)
                    dist1 = (i+diff[0],j+diff[1])
                    if 0 <= dist1[0] < rowSize and 0 <= dist1[1] < colSize:
                        antinodes.add(dist1)
                    antinodes2.add((x,y))
                    antinodes2.add((i,j))
                    while 0 <= dist1[0] < rowSize and 0 <= dist1[1] < colSize:
                        antinodes2.add(dist1)
                        dist1 = (dist1[0]+diff[0],dist1[1]+diff[1])
                    diff = (x-i,y-j)
                    dist2 = (x+diff[0],y+diff[1])
                    if 0 <= dist2[0] < rowSize and 0 <= dist2[1] < colSize:
                        antinodes.add(dist2)
                    while 0 <= dist2[0] < rowSize and 0 <= dist2[1] < colSize:
                        antinodes2.add(dist2)
                        dist2 = (dist2[0]+diff[0],dist2[1]+diff[1])
                satellites[lines[i][j]].append((i,j))
print(len(antinodes))
print(len(antinodes2))




                
            

    