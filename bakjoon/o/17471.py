# https://www.acmicpc.net/problem/17471
# 비트마스크, 그래프, 백트래킹

# N이 최대 10이므로 2^10 = 1024 모든 경우를 다해봐도 된다.


def solve():
    import sys
    input = sys.stdin.readline
    MAX = sys.maxsize
    N = int(input())
    values = list(map(int, input().split()))
    edges = [[0] * N for i in range(N)]
    for i in range(N):
        input_tmp = map(int,input().split())
        next(input_tmp)
        for t in input_tmp:
            edges[i][t - 1] = 1
    

    bit_range = pow(2,N)
    bit_checks = [pow(2,i) for i in range(N)]
    # 첫 0에서 bfs 검증
    # 두번쨰 0에서 bsf 검증
    # 모든 곳을 다 방문했다면 min_Cost 갱신
    def checking(bit_idx, check_number):
        for i in range(N):
            bit_check = bit_checks[i]
            if ((bit_idx & bit_check) > 0) == check_number:
                return i
    def searching(pos, visited,bit_idx, check_number):
        findings = [pos]
        visited[pos]= 1
        while findings:
            cur = findings.pop()
            for i in range(N):
                if not edges[cur][i] or visited[i] or ((bit_idx & bit_checks[i]) > 0) != check_number:
                    continue
                visited[i] = 1
                findings.append(i)
    def calc(bit_idx):
        a = 0
        b= 0
        for i in range(N):
            bit_check = bit_checks[i]
            if bit_idx & bit_check:
                a += values[i]
            else:
                b += values[i]
        return abs(a-b)
    result = MAX
    # 1 ~ 111110
    for bit_idx in range(1, bit_range - 1):
        visited = [0] * N
        a_pos = checking(bit_idx, 0)
        b_pos = checking(bit_idx, 1)
        searching(a_pos,visited,bit_idx,0 )
        searching(b_pos,visited,bit_idx,1 )
        if 0 in visited:
            continue
        else:
            result = min(result, calc(bit_idx))
    if result == MAX:
        return -1
    else:
        return result
print(solve())