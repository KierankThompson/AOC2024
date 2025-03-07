from collections import defaultdict
rules = defaultdict(list)
with open("problem5_1.txt") as f:
    lines = f.read().splitlines()
    for line in lines:
        key,value = line.split("|")
        rules[key].append(value)
pageSum = 0
incPageSum = 0
with open("problem5_2.txt") as f:
    lines = f.read().splitlines()
    for line in lines:
        seen = set()
        isValid = True
        nLine = line.split(",")
        for num in nLine:
            for prev in seen:
                if prev in rules[num]:
                    isValid = False
                    break
            seen.add(num)
        if isValid:
            pageSum += int(nLine[len(nLine)//2])
        else:
            nLine.sort(key=lambda x: sum([1 if i in rules[x] else 0 for i in seen]))
            incPageSum += int(nLine[len(nLine)//2])
print(pageSum)
print(incPageSum)
