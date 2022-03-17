import sys
input = sys.stdin.readline
MAX = 20001

def solve(graph, V,E):
    color = [0] * MAX

    def dfs(key):

        # 인접한 정점이 없음
        if len(graph[key]) == 0:
            return True
        
        for nxt in graph[key]:
        
            # 두 정점 모두 처음 체크
            if (not color[key] and not color[nxt]):
            
                color[key] = 1
                color[nxt] = -1
                return dfs(nxt)
            
            # 두 정점 모두 이전에 체크
            elif (color[key] and color[nxt]):
                if (color[key] == color[nxt]):
                    return False
            # key만 이전에 체크
            elif (color[key]):
                color[nxt] = -color[key]
                return dfs(nxt)
            # nxt만 이전에 체크
            else:
                color[key] = -color[nxt]
        return True
    

    for i in range(V):
        if (not dfs(i)):
            return False
    return True
def solve_b(graph, V, E):
    checkings = [0] * (MAX+1)
    check = 1
    def check_two(i):
        findings = [i]
        while findings:
            cur = findings.pop()
            if not checkings[cur]: 
                checkings[cur] = 1
            for key in graph[cur]:
                if not checkings[key]:
                    findings.append(key)
                if checkings[cur] ==checkings[key]:
                    return 0    
                else:
                    checkings[key] = -checkings[cur]
                
                
        return 1
    for i in range(1, V+1):
        if not check_two(i):
            check = 0
            break
    if check:
        return True
    else:
        return False
    

def main():
    import random
    while True:
        
        graph = [[] for i in range(MAX)]
        V,E = random.randint(4, 5), random.randint(5,10)
        tmp = []
        #입력
        i = 0
        visited = [[0] * (E + 1) for i in range(E+ 1)]
        while i < V:
            u,v = random.randint(1, E), random.randint(1, E)
            
            if u == v or visited[u][v] or visited[v][u]:
                continue
            visited[v][u] = 1
            visited[u][v] = 1
            tmp.append((u,v))
            graph[u].append(v)
            graph[v].append(u)
            i += 1
        if solve(graph, V,E) == solve_b(graph, V, E):
            continue
        else:
            print(solve(graph, V,E) ,solve_b(graph, V, E))
            print(1)
            
            print(V,E)
            for a,b, in tmp:
                print(a,b)
            break
main()


