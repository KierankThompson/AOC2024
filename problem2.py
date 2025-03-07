def testArr(arr):
    isSafe = True
    increasing = False
    if int(arr[0]) < int(arr[1]):
        increasing = True
    for i in range(len(arr)-1):
        diff = int(arr[i+1]) - int(arr[i])
        if increasing:
            if not 1 <= diff <= 3:
                isSafe = False
                break
        else:
            if not -3 <= diff <= -1:
                isSafe = False
                break
    if isSafe:
        return 1
    else:
        return 0





safeCount = 0
with open("problem2.txt") as f:
    lines = f.readlines()
    for line in lines:
        arr = line.split()
        safeCount += testArr(arr)
print(f"Part 1 Answer: {safeCount}")









safeCount = 0
with open("problem2.txt") as f:
    lines = f.readlines()
    for line in lines:
        arr = line.split()
        results = [testArr(arr),testArr(arr[1:])]
        for i in range(1,len(arr)):
            results.append(testArr(arr[:i] + arr[i+1:]))
        if any(results):
            safeCount += 1
        
print(f"Part 2 Answer: {safeCount}")
