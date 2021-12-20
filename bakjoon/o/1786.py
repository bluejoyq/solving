T = input()
P = input()
N = len(T)
M = len(P)
lps = [0] * M

idx = 1
max_pre_length = 0 
while idx < M:
    if P[idx] == P[max_pre_length]:
        max_pre_length += 1
        lps[idx] = max_pre_length
        idx += 1
    elif max_pre_length > 0:
        max_pre_length = lps[max_pre_length - 1]
    else:
        lps[idx] = max_pre_length
        idx += 1

a = 0
b = 0

result = []
while a < N:
    if T[a] == P[b]:
        if b == M-1:
            result.append(a - M + 2)
            b = lps[b]
            a += 1
            continue
        a += 1
        b += 1
    else:
        
        if b == 0:
            a+= 1
            continue
        b = lps[b - 1]
print(len(result)) 
print(*result)