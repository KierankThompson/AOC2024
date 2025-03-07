from collections import Counter
l1 = []
l2 = []
with open("problem1.txt") as f:
    lines = f.readlines()
    for line in lines:
        nums = line.split()
        l1.append(nums[0])
        l2.append(nums[1])
dist = 0
for num1,num2 in zip(sorted(l1),sorted(l2)):
    dist += abs(int(num1)-int(num2))
print(f"Part 1 Answer: {dist}")


lineTwoCount = Counter(l2)
freqMult = 0
for num in l1:
    freqMult += int(num) * lineTwoCount.get(num,0)
print(f"Part 2 Answer: {freqMult}")

