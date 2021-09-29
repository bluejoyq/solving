# 15분
# [1차] 다트 게임 https://programmers.co.kr/learn/courses/30/lessons/17682
def solution(dartResult):
    idx = 0
    scores = []
    multiple_by_char = {"S":1,"D":2,"T":3}
    for i in range(3):
        
        cur = dartResult[idx:]
        if cur[1] == "0":
            cur = cur[1:]
            idx += 1
            scores.append(10 ** multiple_by_char[cur[1]])
        else:
            scores.append(int(cur[0]) ** multiple_by_char[cur[1]])
        try:
            if cur[2]  == "#":
                scores[i] *= -1
            elif cur[2] == "*":
                scores[i] *= 2
                if i > 0:
                    scores[i-1] *= 2
            else:
                idx -= 1
        except:
            continue
            
        idx += 3
    answer = sum(scores)
    return answer