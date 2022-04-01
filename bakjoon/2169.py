import sys
input = sys.stdin.readline
MAX = sys.maxsize

N, M = map(int,input().split())
def input_values():
    return [list(map(int,input().split())) for i in range(N)]

def is_valid(r,c):
    if r > N - 1 or c > M - 1 or c < 0: 
        return 0
    return 1
def is_small(r,c,can_left, visited, val):
    if visited[r][c][can_left] < val:
        return 0
    return 1
def dfs(values):
    from heapq import heappop, heappush
    visited = [[[MAX,MAX] for j in range(M)] for i in range(N)]
    findings = []
    # val, r,c, can_left?
    heappush(findings, (-values[0][0], 0,0, 1))
    def check_and_go(r,c, new_can_left, cur_val):
        try:
            new_val = cur_val- values[r][c]
        except:
            new_val = 0
        if is_valid(r,c) and is_small(r,c, new_can_left,visited, new_val):
            visited[r][c][new_can_left] = new_val
            heappush(findings,(new_val,r, c, new_can_left))
    while findings:
        cur_val, r,c, can_left= heappop(findings)

        if visited[r][c][can_left] < cur_val:
            continue
        visited[r][c][can_left] = cur_val 
        check_and_go(r+1,c,1, cur_val)
        check_and_go(r,c + 1,0, cur_val)
        if can_left:
            check_and_go(r,c - 1,1, cur_val)

    return visited[N-1][M-1][1]
def main():
    values = input_values()
    return dfs(values)
    
print(main())