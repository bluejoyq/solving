L = int(input())
strings = input()


cur_idx = 1
cur_comparing = 0
lps = [0] * L
while cur_idx < L:
    if strings[cur_idx] == strings[cur_comparing]:
        cur_comparing += 1
        lps[cur_idx] = cur_comparing
        cur_idx += 1
    elif cur_comparing > 0:
        cur_comparing = lps[cur_comparing - 1]
    else:
        lps[cur_idx] = cur_comparing
        cur_idx += 1

print(lps)