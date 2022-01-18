import random
from collections import deque
def solve(a,b,c):

    a_idx = 0
    b_idx = 0
    visited = [[0] * (len(b) + 1) for i in range(len(a) + 1)]
    candidates = deque([(0, a_idx,b_idx)])
    
    while candidates:
        c_idx, a_idx, b_idx = candidates.pop()
        if a_idx < len(a) and a[a_idx] == c[c_idx]:
            if c_idx + 1 == len(c):
                return 1
            if visited[a_idx + 1][b_idx]:
                continue
            visited[a_idx + 1][b_idx]=1
            candidates.append((c_idx + 1,a_idx + 1, b_idx))
        if b_idx < len(b) and b[b_idx] == c[c_idx]:
            
            if c_idx + 1 == len(c):
                return 1
            if visited[a_idx][b_idx + 1]:
                continue
            visited[a_idx][b_idx + 1] = 1 
            candidates.append((c_idx + 1,a_idx, b_idx + 1))
    return 0
string_pool = 'abcd'
while True:
    a_len = random.randint(3, 100)
    b_len = random.randint(3,100)
    a = ""
    b = ""
    c = ""
    for i in range(a_len):
        a += random.choice(string_pool)
    for i in range(b_len):
        b += random.choice(string_pool)
    
    a_i = 0
    b_i = 0
    for i in range(a_len + b_len):
        if b_i >= b_len or (a_i < a_len and random.randint(1,2)) == 1:
            c += a[a_i]
            a_i += 1
        elif b_i < b_len:
            c += b[b_i]
            b_i += 1
    if solve(a,b,c):
        print(a,b,c)
        continue
    else:
        print(a)
        print(b)
        print(c)
        break