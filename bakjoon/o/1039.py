N,K = map(int,input().split())
visited =[set([]) for i in range(K + 1)] 
N = str(N)
visited[0].add(N)

M = len(list(N))
def change(num_set, cur):
    cur = list(cur)
    for i in range(M - 1):
        for j in range(i + 1, M):
            if i == 0 and cur[j] == '0':
                continue
            # str이라 부호 반대
            nxt = cur[:]
            nxt[i], nxt[j] = nxt[j], nxt[i]
            num_set.add("".join(nxt))
def solve():
    for i in range(K):
        for cur in visited[i]:
            change(visited[i + 1], cur)
            if visited[i+1]:
                continue
            return -1
    return visited[K]

result = solve()
if result == -1:
    print(-1)
else:
    result = list(map(int, result))
    print(max(result))