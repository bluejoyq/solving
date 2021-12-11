#

def nextMove(n,r,c,grid):
    princess = []
    for rr in range(n):
        for cc in range(n):
            if grid[rr][cc] == 'p':
                princess = [rr,cc]
                break
    col_gap = r - princess[0]
    row_gap = c - princess[1]
    if col_gap > 0:
        return('UP')
    elif col_gap < 0:
        return('DOWN')
    if row_gap > 0:
        return('LEFT')
    elif row_gap < 0:
        return('RIGHT')

n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))