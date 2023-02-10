board = []
R,C = map(int, input().split())
for i in range(R):
    row = input()
    board.append(row)

def get_bit_ord(ch):
    return 1 << (ord(ch) - 65 )

def is_valid(nxt_r,nxt_c, visited):
    if R > nxt_r > -1 and C > nxt_c > -1 and not(visited & get_bit_ord(board[nxt_r][nxt_c])):
        return True
    return False


cache = [[{} for i in range(C)] for j in range(R)]
routes = [(0,1), (0,-1), (1,0), (-1, 0)]

findings = [(0,0,get_bit_ord(board[0][0]),1)]

result = 0
while findings:
    
    cur_r, cur_c, visited, val = findings.pop()
    result = max(result, val)
    for r_p, c_p in routes:
        nxt_r = cur_r + r_p
        nxt_c = cur_c + c_p
        if not is_valid(nxt_r, nxt_c, visited):
            continue

        if visited in cache[nxt_r][nxt_c] and cache[nxt_r][nxt_c][visited] <= val:
            continue
        cache[nxt_r][nxt_c][visited] = val
        findings.append((nxt_r, nxt_c, visited | get_bit_ord(board[nxt_r][nxt_c]), val+ 1))

print(result)