# 3시 15분 ~ 5시 ㅡㅡ 졸려서 못풀겠음
# [1차] 추석 트래픽 https://programmers.co.kr/learn/courses/30/lessons/17676

def solution(lines):
    from datetime import datetime, timedelta

    N = len(lines)
    answer = 1
    datas = [0] * N
    for i in range(N):
        line = lines[i]
        D, S, T = line.split()
        T = T.replace("s", "")
        TT = list(map(int,T.split(".")))
        milliT = TT[0] * 1000
        if len(TT) > 1:
            milliT += TT[1]
        end_time = datetime.strptime(D + " " + S, "%Y-%m-%d %H:%M:%S.%f")
        
        start_time = end_time - timedelta(milliseconds = milliT - 1)
        
        datas[i] = [start_time, end_time]
    
    left = 0
    right = 1

    while right < N:
        
        if datas[left][1] + timedelta(seconds = 1) > datas[right][0]:
            while right < N and datas[left][1]  + timedelta(seconds = 1)  > datas[right][0]:
                right += 1
            
        else:
            left += 1
        answer = max(answer, right - left)
    return answer
print(solution([
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]))