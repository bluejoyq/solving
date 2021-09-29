def solution(fees, records):
    from math import ceil
    def get_fee(taken_time):
        
        result = 0
        if taken_time > fees[0]:
            result = (ceil((taken_time - fees[0]) / fees[2]) * fees[3] )+ fees[1]
        else:
            result = fees[1]
        return result
    
    N = len(records)
    answer = []
    cache = [0] * 10000
    in_time = [-1] * 10000
    for i in range(N):
        rTime, number, flag = records[i].split()
        number = int(number)
        tmp = list(map(int,rTime.split(":")))
        rTime_by_min = tmp[0] * 60 + tmp[1]
        if flag == "IN":
            in_time[number] = rTime_by_min
        else:
            taken_time = rTime_by_min - in_time[number]
            in_time[number] = -1
            cache[number] += taken_time
    last = 23 *60 + 59
    for i in range(10000):
        if in_time[i] == -1:
            continue
        
        taken_time = last - in_time[i]
        cache[i] += taken_time
    for c in cache:
        if c ==0:
            continue
        answer.append(get_fee(c))
    return answer
a = solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])
print(a)