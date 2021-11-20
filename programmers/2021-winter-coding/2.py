def solution(time, gold, upgrade):
    up_num = len(upgrade)
    answer = -1
    for up_max in range(up_num):
        t = 1
        cur_gold = cur_upgrade = 0
        left_second = upgrade[0][1]
        while t < time + 1:
            while cur_upgrade < up_max and cur_gold >= upgrade[cur_upgrade + 1][0]:
                cur_upgrade += 1
                cur_gold -= upgrade[cur_upgrade][0]

            left_second = upgrade[cur_upgrade][1]

            if t + left_second > time + 1:
                break
            cur_gold += gold
            t += left_second 
        answer = max(answer, cur_gold)
    return answer