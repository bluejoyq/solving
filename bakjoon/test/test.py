n=int(input())
a, b=map(int, input().split())
m=int(input())
graph=[[] for _ in range(n+1)]
visited=[0 for _ in range(n+1)]
ls=[]
for _ in range(m):
        n1, n2=map(int, input().split())
        graph[n1].append(n2)
        graph[n2].append(n1)
        
def dfs(graph, start, visited):
    visited[start]=1
    ls.append(start)
    for i in graph[start]:
        if visited[i]==0:
            dfs(graph, i, visited)

dfs(graph, a, visited)
dist=[]
if b not in ls:
    print(-1)
else:
    for i in graph[a]:
        d=ls.index(b)-ls.index(i)
        dist.append(d)
    print(min(dist)+1)