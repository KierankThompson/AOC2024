import time

start = time.time()
def possibleValues(arr,curArr,concat=False):
    if not arr:
        return curArr
    arr2 = []
    for num in curArr:
        arr2.append(num*int(arr[0]))
        arr2.append(num+int(arr[0]))
        if concat:
            arr2.append(int(f"{num}{arr[0]}"))
    return possibleValues(arr[1:],arr2,concat)



calibrationTotal = 0
calibrationTotal2 = 0
with open("problem7.txt") as f:
    lines = f.read().splitlines()
    for line in lines:
        arr = line.split(":")
        inputArr = arr[1].split()
        arr2 = possibleValues(inputArr[1:],[int(inputArr[0])])
        if int(arr[0]) in arr2:
            calibrationTotal += int(arr[0])
        arr3 = possibleValues(inputArr[1:],[int(inputArr[0])],True)
        if int(arr[0]) in arr3:
            calibrationTotal2 += int(arr[0])
end = time.time()
print(calibrationTotal)
print(calibrationTotal2)


