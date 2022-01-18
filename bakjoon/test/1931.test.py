def solve_wrong(N,raw_values):
    time_list = []
    for i in range(N):
        time_list.append(raw_values[i])
    time_list.sort()

    select_list = [time_list[0]]
    for time in time_list[1:]:
        # 시작 시간이 크고 종료 시간이 작다면 교체
        if (select_list[-1][0] <= time[0]) and (time[1] <= select_list[-1][1]):
            select_list[-1] = time
        # 시작 시간이 크고 종료 시간이 크다면 새로 추가
        elif (time[0] >= select_list[-1][1]) and (time[1] >= select_list[-1][1]):
            select_list.append(time)
    return len(select_list)


def solve(N, raw_values):
    values = [0] * N
    for i in range(N):
      values[i] = list(raw_values[i][::-1])
    values.sort()

    end = -1
    count = 0
    for i in range(N):
      if end <= values[i][1]:
        end = values[i][0]
        count += 1
    return(count)


import random
while True:
    N = random.randint(4, 10)
    raw_values = [0] *N
    for i in range(N):
        a = random.randint(0,10) 
        b = random.randint(a,10)
        raw_values[i] = [a,b]
    result_a = solve_wrong(N,raw_values)
    result_b = solve(N,raw_values)
    if result_a != result_b:
        print(N)
        print(raw_values)
        print(result_a,result_b)
        break