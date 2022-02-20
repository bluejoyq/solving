H,W = map(int, input().split())

values = list(map(int, input().split()))
visited= [[0]*W for i in range(H)]

for hh in range(H -1, -1, -1):
    for ww in range(W):
        if values[ww] - 1 >= hh or visited[hh][ww]:
            break
        visited[hh][ww] = 1
for hh in range(H - 1, -1, -1):
    for ww in range(W -1,-1,-1 ):
        if values[ww] - 1>= hh or visited[hh][ww]:
            break
        visited[hh][ww] = 1
print(H*W - sum(values) 
    - sum([sum(v) for v in visited]))