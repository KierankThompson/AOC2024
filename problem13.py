import re




def search(aButtonX, aButtonY, bButtonX, bButtonY, prizeX, prizeY):
    det = aButtonX * bButtonY - bButtonX * aButtonY
    a = (prizeX * bButtonY - prizeY * bButtonX) // det
    b = (prizeY * aButtonX - prizeX * aButtonY) // det
    if a * aButtonX + b * bButtonX == prizeX and a * aButtonY + b * bButtonY == prizeY:
        return (3 * a) + b
    return 0


arr = []
with open("problem13.txt") as f:
    arr = f.read().splitlines()
buttonP = re.compile(r"X\+(\d+), Y\+(\d+)")
prizeP =  re.compile(r"X=(\d+), Y=(\d+)")
ans = 0
ans2 = 0
for i in range(0,len(arr),4):
    aButton = buttonP.search(arr[i]).groups()
    bButton = buttonP.search(arr[i+1]).groups()
    prize = prizeP.search(arr[i+2]).groups()
    aButtonX, aButtonY = int(aButton[0]), int(aButton[1])
    bButtonX, bButtonY = int(bButton[0]), int(bButton[1])
    prizeX, prizeY = int(prize[0]), int(prize[1]) 
    count1 = search(aButtonX,aButtonY,bButtonX,bButtonY,prizeX,prizeY)
    count2 = search(aButtonX,aButtonY,bButtonX,bButtonY,prizeX+10000000000000,prizeY+10000000000000)
    ans += count1
    ans2 += count2

print(ans)
print(ans2)

        

        
    
