xMasCount = 0
xMaxCount2 = 0
with open("problem4.txt") as f:
    lines = f.read().splitlines()
    numRows = len(lines)
    numCols = len(lines[0])
    for i in range(numRows):
        for j in range(numCols):
            if j + 3 < numCols:
                curStr = "".join(lines[i][j+k] for k in range(4))
                if curStr == "XMAS" or curStr == "SAMX":
                    xMasCount += 1
            if i + 3 < numRows:
                curStr = "".join(lines[i+k][j] for k in range(4))
                if curStr == "XMAS" or curStr == "SAMX":
                    xMasCount += 1
            if i + 3 < numRows and j + 3 < numCols:
                    curStr = "".join(lines[i+k][j+k] for k in range(4))
                    if curStr == "XMAS" or curStr == "SAMX":
                        xMasCount += 1
            if i + 3 < numRows and j - 3 >= 0:
                curStr = "".join(lines[i+k][j-k] for k in range(4))
                if curStr == "XMAS" or curStr == "SAMX":
                    xMasCount += 1
            if i + 1 < numRows and i - 1 >= 0 and j + 1 < numCols and j - 1 >= 0:
                curStr1 = "".join(lines[i-1+k][j-1+k] for k in range(3))
                curStr2 = "".join(lines[i-1+k][j+1-k] for k in range(3))
                if (curStr1 == "MAS" or curStr1 == "SAM") and (curStr2 == "MAS" or curStr2 == "SAM"):
                    xMaxCount2 += 1

print(xMasCount)
print(xMaxCount2)

