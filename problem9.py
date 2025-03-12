from collections import defaultdict
import time


start = time.time()
arr = []
with open("problem9.txt") as f:
    diskMap = f.read()
    curID = 0
    for i in range(0,len(diskMap)):
        if not i % 2:
            for j in range(int(diskMap[i])):
                arr.append(curID)
            curID += 1
        else:
            for j in range(int(diskMap[i])):
                arr.append(".")


bot = 0
top = len(arr) - 1
while bot < top:
    while bot < top and arr[bot] != ".":
        bot += 1
    while top > bot and arr[top] == ".":
        top -= 1
    arr[bot] = arr[top]
    arr[top] = "."
i = 0
ans = 0
while arr[i] != ".":
    ans += arr[i] * i
    i += 1
print(ans)
end = time.time()
print(end-start)


start = time.time()
ans = 0
freeSpaceHeap = []
fileDic = defaultdict(list)
arr = []
with open("problem9.txt") as f:
    arrIndex = 0
    curID = 0
    diskmap = f.read()
    for i in range(0,len(diskMap)):
        if not i % 2:
            for j in range(int(diskMap[i])):
                arr.append(curID)
            fileDic[int(diskMap[i])].append((arrIndex,curID))
            curID += 1
        else:
            for j in range(int(diskMap[i])):
                arr.append(".")
            freeSpaceHeap.append((arrIndex,int(diskMap[i])))
        arrIndex += int(diskMap[i])
while freeSpaceHeap:
    index,space = freeSpaceHeap.pop(0)
    fits = []
    for spaces in range(space,0,-1):
        if fileDic[spaces] and fileDic[spaces][-1][0] > index:
            fits.append((fileDic[spaces][-1][0],spaces))
    if fits:
        bestFit = max(fits)[1]
        fileIndex,curFile = fileDic[bestFit].pop()
        for i in range(bestFit):
            arr[index+i] = curFile
            arr[fileIndex+i] = "."
        if bestFit != space:
            freeSpaceHeap.insert(0,(index+bestFit,space-bestFit))
for i,ele in enumerate(arr):
    if ele != ".":
        ans += i * int(ele)
print(ans)
end = time.time()
print(end-start)






    








