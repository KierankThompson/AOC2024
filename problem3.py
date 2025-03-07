import re

ans = 0
with open("problem3.txt") as f:
    lines = f.readlines()
    p = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    for line in lines:
        for match in p.findall(line):
            ans += int(match[0]) * int(match[1])
print(ans)
ans = 0
with open("problem3.txt") as f:
    lines = f.readlines()
   
    enabled = True
    for line in lines:
        for match in re.finditer(r"do\(\)|don't\(\)|mul\((\d{1,3}),(\d{1,3})\)",line):
            if match[0] == "don't()":
                enabled = False
            elif match[0] == "do()":
                enabled = True
            else:
                if enabled:   
                    ans += int(match[1]) * int(match[2])
print(ans)



        