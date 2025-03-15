import re

robots = []
rowSize = 103
colSize = 101
lines = []
with open("problem14.txt") as f:
    lines = f.read().splitlines()
for line in lines:
    pos,velocity = re.findall(r"=(-?\d{1,3}),(-?\d{1,3})",line)
    x,y = pos
    vX, vY = velocity
    newX = (int(x)+int(vX)*100) % rowSize
    newY = (int(y)+int(vY)*100) % colSize
    robots.append((newX,newY))
