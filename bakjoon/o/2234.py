import sys
input = sys.stdin.readline

N,M = map(int, input().split())
board = [list(map(int,input().split())) for i in range(M)]


visited = [[0] * N for i in range(M)]
can_go = [[1,0,8], [-1,0,2], [0,1,4],[0,-1, 1]]

rooms = []

def find_room(start_r,start_c):
    findings = [(start_r,start_c)]
    room_size = 0
    room_idx = len(rooms)
    while findings:
        r,c = findings.pop()
        if visited[r][c]:
            continue
        room_size += 1
        visited[r][c] = room_idx + 1
        for r_plus, c_plus, check in can_go:
            nxt_r = r + r_plus
            nxt_c = c + c_plus
            if nxt_r < 0 or nxt_r > M-1 or nxt_c < 0 or nxt_c > N-1:
                continue
            if visited[nxt_r][nxt_c] or board[r][c] & check:
                continue
            findings.append((r+r_plus, c + c_plus))
    rooms.append(room_size)

for r in range(M):
    for c in range(N):
        if visited[r][c]:
            continue
        find_room(r,c)

R = len(rooms)
max_result = 0
for r in range(M):
    for c in range(N):
        cur_room = visited[r][c] - 1
        for r_plus, c_plus, check in can_go:
            nxt_r = r + r_plus
            nxt_c = c + c_plus
            if nxt_r < 0 or nxt_r > M-1 or nxt_c < 0 or nxt_c > N-1:
                continue
            nxt_room = visited[nxt_r][nxt_c] - 1
            if nxt_room == cur_room:
                continue
            max_result = max(max_result, rooms[cur_room] + rooms[nxt_room])
print(len(rooms))
print(max(rooms))
print(max_result)