import time
import math
from collections import defaultdict



def checkDigits(number):
    return int(math.log10(number))+1


def splitNum(number):
    digits = int(math.log10(number))+1
    num1, num2 = 0,0
    for i in range(digits//2):
        num2 += number % 10 * 10**i
        number //= 10
    for i in range(digits//2):
        num1 += number % 10 * 10**i
        number //= 10
    return num1,num2
    


ans = 0
arr = []
with open("problem11.txt") as f:
    arr = list(map(int,f.readlines()[0].split()))
dic = defaultdict(int)
for ele in arr:
    dic[ele] += 1
n = 75
start = time.time()
seen = {0:1}
for i in range(n):
    newDic = defaultdict(int)
    roundStart = time.time()
    for num in dic: 
        if num in seen:
            if isinstance(seen[num],int):
                newDic[seen[num]] += dic[num]
            else:
                newDic[seen[num][0]] += dic[num]
                newDic[seen[num][1]] += dic[num]
        elif not checkDigits(num) % 2:
            newNum = splitNum(num)
            newDic[newNum[0]] += dic[num]
            newDic[newNum[1]] += dic[num]
            seen[num] = newNum
        else:
            newDic[num*2024] += dic[num]
            seen[num] = num*2024
    dic = newDic
    end = time.time()
    print(f"Iteration {i+1} took {end-roundStart} seconds")
end = time.time()
print(f"Total time of {end-start} seconds")
for value in dic.values():
    ans += value
print(ans)

