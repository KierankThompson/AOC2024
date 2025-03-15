import re




robots = []
rowSize = 103
colSize = 101


def calculateSafety(robotArr):
    quad = [0,0,0,0]
    for x,y in robotArr:
        if x < colM:
            if y < rowM:
                quad[0] += 1
            elif y > rowM:
                quad[2] += 1
        elif x > colM:
            if y < rowM:
                quad[1] += 1
            elif y > rowM:
                quad[3] += 1
    return quad[0]  * quad[1] * quad[2] * quad[3]

def calculateCloseness(robotArr):
    score = 0
    for x,y in robotArr:
        if (x+1,y) in robotArr:
            score += 1
        if (x-1,y) in robotArr:
            score += 1
        if (x,y+1) in robotArr:
            score += 1
        if (x,y-1) in robotArr:
            score += 1
    return score
    


lines = []
with open("problem14.txt") as f:
    lines = f.read().splitlines()
for line in lines:
    pos,velocity = re.findall(r"=(-?\d{1,3}),(-?\d{1,3})",line)
    x,y = pos
    vX, vY = velocity
    newX = (int(x)+int(vX)*100) % colSize
    newY = (int(y)+int(vY)*100) % rowSize
    robots.append((newX,newY))
rowM = rowSize // 2 
colM = colSize // 2 
ans1 = calculateSafety(robots)
print(ans1)



class Robot():
    def __init__(self,x,y,vX,vY,colSize,rowSize):
        self.x = x
        self.y = y
        self.vX = vX
        self.vY = vY
        self.colSize = colSize
        self.rowSize = rowSize

    def update(self):
        self.x = (self.x + self.vX) % self.colSize
        self.y = (self.y + self.vY) % self.rowSize
    def __str__(self):
        return f"({self.y}, {self.x})"
    def __repr__(self):
        return self.__str__()

robots = []
for line in lines:
    pos,velocity = re.findall(r"=(-?\d{1,3}),(-?\d{1,3})",line)
    x,y = pos
    vX, vY = velocity
    robots.append(Robot(int(x),int(y),int(vX),int(vY),colSize,rowSize))

iterations = 0
ans2 = 0
for i in range(10000):
        robSet = set()
        for j,robot in enumerate(robots):
            robSet.add((robot.x,robot.y))
            robots[j].update()
        safety = calculateCloseness(robSet)
        if safety > ans2:
            ans2 = safety
            iterations = i

        
print(ans2)
print(iterations)



                





