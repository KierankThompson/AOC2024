import curses
import time
import math

def main(stdscr):

    arr = []
    warehouse = {}
    directions = []

    with open("problem15.txt") as f:
        arr = f.read().splitlines()

    curX = 0
    curY = 0
    mode = 0
    for i,line in enumerate(arr):
        if not line:
            mode = 1
        for j,ch in enumerate(line):
            if mode == 0:
                if ch == "@":
                    curX = i
                    curY = j
                elif ch != '.':
                    warehouse[(i,j)] = ch
            else:
                directions.append(ch)
    dirDic = {"^":(-1,0),"v":(1,0),">":(0,1),"<":(0,-1)}

    for d in directions:
        moveStack = []
        tempX = curX + dirDic[d][0]
        tempY = curY + dirDic[d][1]
        while (tempX,tempY) in warehouse:
            if warehouse[(tempX,tempY)] == "#":
                moveStack.append((-1,-1))
                break
            else:
                moveStack.append((tempX,tempY))
            tempX += dirDic[d][0]
            tempY += dirDic[d][1]
        if moveStack and moveStack[-1] == (-1,-1):
            continue
        for box in moveStack[::-1]:
            warehouse[(box[0]+dirDic[d][0],box[1]+dirDic[d][1])] = warehouse.pop(box)
        curX += dirDic[d][0]
        curY += dirDic[d][1]
    ans = 0
    for x,y in warehouse:
        if warehouse[(x,y)] == "O":
            ans += 100 * x + y
    print(ans)



    warehouse = {}
    curX = 0
    curY = 0
    mode = 0
    rowSize = 0
    colSize = 0
    for i,line in enumerate(arr):
        if not line:
            break
        rowSize = max(rowSize, i)
        for j,ch in enumerate(line):
            if ch == "@":
                curX = i
                curY = j*2
            elif ch == '#':
                warehouse[(i,j*2)] = ch
                warehouse[(i,j*2+1)] = ch
            elif ch == 'O':
                warehouse[(i,j*2)] = "["
                warehouse[(i,j*2+1)] = "]"
            colSize = max(colSize,j)
    for d in directions:
        stdscr.clear()
        moveStack = []
        tempX = curX + dirDic[d][0]
        tempY = curY + dirDic[d][1]
        if d == '<' or d == ">":
            while (tempX,tempY) in warehouse:
                if warehouse[(tempX,tempY)] == "#":
                    moveStack.append((-1,-1))
                    break
                else:
                    moveStack.append((tempX,tempY))
                tempX += dirDic[d][0]
                tempY += dirDic[d][1]
            if moveStack:
                if moveStack[-1] == (-1,-1):
                    continue
            for box in moveStack[::-1]:
                warehouse[(box[0]+dirDic[d][0],box[1]+dirDic[d][1])] = warehouse.pop(box)
        else:
            queue = [(curX,curY)]
            seen = set()
            while queue:
                tempX,tempY = queue.pop()
                seen.add((tempX,tempY))
                tempX += dirDic[d][0]
                if (tempX,tempY) in warehouse:
                    if warehouse[(tempX,tempY)] == "#":
                        moveStack.append((-1,-1))
                        break
                    else:
                        if (tempX,tempY) not in seen:
                            queue.append((tempX,tempY))
                            moveStack.append((tempX,tempY))
                            if warehouse[(tempX,tempY)] == '[':
                                queue.append((tempX,tempY+1))
                                moveStack.append((tempX,tempY+1))
                            elif warehouse[(tempX,tempY)] == ']':
                                queue.append((tempX,tempY-1))
                                moveStack.append((tempX,tempY-1))
            if (moveStack and moveStack[-1] == (-1,-1)):
                continue
            moveStack.sort(key = lambda x: x[0],reverse=(d=="v"))
            for box in moveStack:
                warehouse[(box[0]+dirDic[d][0],box[1]+dirDic[d][1])] = warehouse.pop(box)
        curX += dirDic[d][0]
        curY += dirDic[d][1]
        arrAns = [["." for _ in range(colSize*2+2)] for _ in range(rowSize+1)]
        for key in warehouse:
            arrAns[key[0]][key[1]] = warehouse[key]
        arrAns[curX][curY] = "@"
        max_y, _ = stdscr.getmaxyx()
        mult = math.ceil(len(arrAns) / max_y)
        start = 0
        for m in range(mult):
            if curX < (m+1) * max_y:
                start = m*max_y
                break

        start_y = max(start, 0)
        end_y = min(start_y + max_y, len(arrAns))
        for i in range(start_y,end_y):
            stdscr.addstr(i-start_y, 5, ''.join(arrAns[i]))
        stdscr.refresh()
        time.sleep(0.05)

    ans2 = 0
    total = 0
    for x,y in warehouse:
        if warehouse[(x,y)] == "[":
            total += 1
            ans2 += 100 * x + y
    print(ans2)



curses.wrapper(main)

        











        


