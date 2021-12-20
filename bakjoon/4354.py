# 백만 글자에 대해서 1~10^6을 다해본다.


def solve(s):
    L = len(s)

    cur_idx = 1
    cur_length = 1
    last = 0
    while cur_idx < L:
        if s[cur_idx] == s[last]:
            last += 1
            cur_idx += 1
            
        elif cur_idx > L // 2:
            cur_length = L
            break
        elif last > 0:
            last -= 1
            cur_length += 1
        else:
            cur_idx += 1
            cur_length += 1

    if last % cur_length == 0:
        print(L // cur_length)
    else:   
        print(1)
while True:
    s = input()

    if s == '.':
        break
    solve(s)