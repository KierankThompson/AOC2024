import re

ans = 0
with open("problem3.txt") as f:
    lines = f.readlines()
    p = re.compile("mul\(\d{1,3},\d{1,3}\)")
    p2 = re.compile("\d{1,3}")
    for line in lines:
        for match in p.findall(line):
            numbers = p2.findall(match)
            ans += int(numbers[0]) * int(numbers[1])
print(ans)

        