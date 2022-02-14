from collections import deque


def solve():
    F,S,G,U,D = map(int, input().split())

    visited = [0]* (F + 1)
    visited[S] = 1
    findings = deque([(0,S)])

    def check_nxt(cost, nxt):
        if nxt < 1 or nxt > F or visited[nxt]:
            return
        visited[nxt] = 1
        findings.append((cost,nxt))

    while findings:
        cost, cur = findings.popleft()
        if cur == G:
            return(cost)
        check_nxt(cost + 1, cur + U)
        check_nxt(cost + 1, cur - D)
    return "use the stairs"

print(solve())