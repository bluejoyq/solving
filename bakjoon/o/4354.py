def solve(s):
    L = len(s)

    cur_idx = 1
    piece_length = 1
    cur_compared = 0
    while cur_idx < L:
        if s[cur_idx] == s[cur_compared]:
            cur_compared += 1
            cur_idx += 1
            continue
        
        # 만약 절반 이상에서 틀렸다면 
        # 더 이상은 조각의 길이를 늘려도 의미가 없다.
        if cur_idx > L // 2:
            piece_length = L
            break

        if cur_compared > 0:
            cur_compared -= 1
        else:
            cur_idx += 1
        
        piece_length += 1

    # 끝까지 비교했는가.
    if cur_compared % piece_length == 0:
        print(L // piece_length)
    else:   
        print(1)
while True:
    s = input()

    if s == '.':
        break
    solve(s)