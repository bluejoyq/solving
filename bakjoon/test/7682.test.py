import sys
input = sys.stdin.readline




result = []
checks = [[0,1,2], [3,4,5], [6,7,8], [0,4,8], [2,4,6], [0,3,6], [1,4,7], [2,5,8]]
exception_case = ['X','O','X','O','X','O','X','O','X']

def is_valid(board):
    x_count = 0
    o_count = 0

    for b in board:
        if b == 'X':
            x_count += 1
        elif b == 'O':
            o_count += 1
    if x_count > 5 or o_count > 4:
        return 0
    if not(x_count == o_count + 1 or o_count == x_count):
        return 0

    x_win = 0
    o_win = 0
    for check in checks:
        start = board[check[0]]
        end_check = 1
        if start == '.':
            continue
        for nxt in check[1:]:
            if start == board[nxt]:
                continue
            end_check = 0
            break
        if not end_check:
            continue
        if start == 'X':
            x_win += 1
        else:
            o_win += 1
    
    if x_win > 0 and o_win > 0:
        return 0
    elif x_win > 0 and x_count == o_count + 1:
        return 1
    elif o_win > 0 and x_count == o_count:
        return 1
    if o_count + x_count == 9:
        return 1
    return 0
def flag(arr,equ):
    #print(arr,equ)
    if arr[0][0]==arr[0][1]==arr[0][2]==equ:
        return True
    if arr[1][0]==arr[1][1]==arr[1][2]==equ:
        return True
    if arr[2][0]==arr[2][1]==arr[2][2]==equ:
        return True
    if arr[0][0]==arr[1][0]==arr[2][0]==equ:
        return True
    if arr[0][1]==arr[1][1]==arr[2][1]==equ:
        return True
    if arr[0][2]==arr[1][2]==arr[2][2]==equ:
        return True
    if arr[0][0]==arr[1][1]==arr[2][2]==equ:
        return True
    if arr[2][0]==arr[1][1]==arr[0][2]==equ:
        return True
    return False
    

def solve(string):
    xcnt=0
    ocnt=0
    index=0
    arr=[[0]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            arr[i][j]=string[index]
            if string[index]=="X":
                xcnt+=1
            if string[index]=="O":
                ocnt+=1
            index+=1
    if xcnt>ocnt+1:
        return(0)
    if ocnt>xcnt:
        return(0)

    if ocnt==xcnt:
        if flag(arr,"O") and not flag(arr,"X"):
            return(1)

    if ocnt+1==xcnt:
        if flag(arr,"X") and not flag(arr,"O"):
            return(1)

    if xcnt==5 and ocnt==4:
        if not flag(arr,"O"):
            return(1)

    return(0)
'''
board = list(input().rstrip()) 
while board[0] != 'e':
    if is_valid(board):
        result.append('valid')
    else:
        result.append('invalid')
    board = list(input().rstrip()) 
print('\n'.join(result))
    
'''
import random
while True:
    tmp = ['.' for i in range(9)]
    visited = [0] * 9
    goal = random.randint(0,9)
    o = goal // 2
    x = goal // 2
    if goal % 2 == 1:
        x += 1
    
    while o > 0 and x > 0:
        cur = random.randint(0, 8)
        if visited[cur]:
            continue
        if o > 0 and x > 0:
            if random.randint(0,1) == 1:
                x -= 1
                tmp[cur] = 'X'
            else:
                o-=1
                tmp[cur] = 'O'
        elif o > 0:
            o-=1
            tmp[cur] = 'O'
        else:
            x -= 1
            tmp[cur] = 'X'
    a = solve(tmp)
    b = is_valid(tmp)
    print(tmp)
    print(a,b)
    if a != b:
        print(tmp)
        print(a,b)
        break