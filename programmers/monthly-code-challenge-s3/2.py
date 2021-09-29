def solution(grid):
    import sys
    sys.setrecursionlimit(1000000)
    n = len(grid)
    m = len(grid[0])
    
    
    # 500 * 500 * 4 100만개임
    # 0은 위, 1은 우측, 2는 아래, 3은 왼쪽
    # 각각에서 나가는 방향으로 ㄱㄱ
    # 모든점을 순회하는 사이클이라면 어느 점에서 보내도 도착한다.
    ways = [[-1,0], [0,1],[1,0], [0,-1]]
    rev_ways = [2,3,0,1]
    left = [3,0,1,2]
    right = [1,2,3,0]
    findings = []
    
    # r,c, 방향, 사이클길이
    answer = []
    visited = [[[0,0,0,0] for c in range(m)] for r in range(n)]
    visited_node = [[0 for c in range(m)] for r in range(n)]
    def check():
        result = 0
        for v in visited_node:
            for p in v:
                if p == 0:
                    return False
                result += p
        return result
    def dfs(r,c,way):
        if visited[r][c][way]:
            return
        visited[r][c][way] = 1
        visited_node[r][c] += 1
        if grid[r][c] == "L":
            way = left[way]
        elif grid[r][c] =="R":
            way = right[way]
        new_r = (r + ways[way][0]) % n
        new_c = (c + ways[way][1]) % m

        if visited[new_r][new_c][way]:
            result = check()
            if result:
                answer.append(result)
            return
            
        
        dfs(new_r,new_c,way)
    for r in range(n):
        for c in range(m):
            for i in range(4):
                dfs(r,c,i)
                visited_node = [[0 for c in range(m)] for r in range(n)]
    return answer
