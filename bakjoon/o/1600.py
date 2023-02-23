import sys
from heapq import heappush ,heappop
MAX = sys.maxsize
K = int(input())
W,H = map(int, input().split())
board = [list(map(int, input().split())) for i in range(H)]


cache = [[[MAX] * (K + 1) for i in range(W)] for j in range(H)]
findings = [(0,K,0,0)]

horse_moves = [(1,2),(2,1),(-1,2),(2,-1),(-2,1),(-2,-1), (1,-2), (-1,-2)]
moves = [(-1,0), (1,0), (0,1), (0,-1)]  



def is_valid(r,c,k, val):
    if -1 < r < H and -1 <c < W and board[r][c] == 0 and cache[r][c][k] > val:
        cache[r][c][k] = val
        return True
    return False
        
result = MAX
while findings:
    cur_val,cur_k,cur_r,cur_c = heappop(findings)
    if cache[cur_r][cur_c][cur_k] < cur_val:
        continue
    if cur_r == H-1 and cur_c == W-1:
        result =cur_val
        break
    for r_plus,c_plus in moves:
        nxt_r = cur_r + r_plus
        nxt_c = cur_c + c_plus
        nxt_val = cur_val+1
        if not is_valid(nxt_r,nxt_c,cur_k, nxt_val):
            continue
        heappush(findings,(nxt_val,cur_k,nxt_r,nxt_c, ))

    if not cur_k:
        continue
    
    for r_plus,c_plus in horse_moves:
        nxt_r = cur_r + r_plus
        nxt_c = cur_c + c_plus
        nxt_val = cur_val+1
        nxt_k = cur_k - 1
        if not is_valid(nxt_r,nxt_c,nxt_k, nxt_val):
            continue
        heappush(findings,(nxt_val,nxt_k,nxt_r,nxt_c))

if result == MAX:
    print(-1)
else:
    print(result)