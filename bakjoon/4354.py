# 백만 글자에 대해서 1~10^6을 다해본다.


def solve(s):
    L = len(s)
    lps = [0] * L
    last_length = 0
    idx = 1
    while idx < L:
        if s[idx] == s[last_length]:
            last_length += 1
            lps[idx] = last_length 
            idx += 1
        else:
            if last_length == 0:
                idx += 1
                continue
            last_length -= 1
    print(lps)

while True:
    s = input()

    if s == '.':
        break
    solve(s)