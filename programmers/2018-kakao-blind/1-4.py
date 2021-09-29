# 24분
# [1차] 셔틀버스 https://programmers.co.kr/learn/courses/30/lessons/17678

def solution(n, t, m, timetable):
    from heapq import heappush, heappop
    watings = []
    for crew in timetable:
        hh,mm = map(int, crew.split(":"))
        heappush(watings, (hh,mm))
    
    answer = [0,0]
    hour = 9
    minute = 0
    for i in range(n):
        for j in range(m):
            if not len(watings):
                answer = [hour,minute]
                break
        
            hh,mm = heappop(watings)
            if hh > hour or (hh == hour and mm > minute):
                heappush(watings, (hh,mm))
                answer = [hour,minute]
                break
            if mm == 0:
                answer = [hh - 1, 59]
            else:
                answer = [hh,mm - 1]
        minute += t
        hour += minute // 60
        minute %= 60
            
    result = ""
    hh = str(answer[0])
    if len(hh) == 1:
        result += "0" + hh
    else:
        result += hh
    result += ":"
    mm = str(answer[1])
    if len(mm) == 1:
        result += "0" + mm
    else:
        result += mm
    return result