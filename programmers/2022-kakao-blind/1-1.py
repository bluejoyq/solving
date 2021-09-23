def solution(id_list, report, k):
    N = len(id_list)
    report_person_checker = {}
    report_counter = {}
    for id in id_list:
        report_person_checker[id] = {}
        report_counter[id] = 0
    
    for r in report:
        id, target = r.split()
        try:
            report_person_checker[id][target]

        except:
            report_person_checker[id][target] = 1
            report_counter[target] += 1
    answer = [0 ] *N
    for i in range(N):
        id = id_list[i]
        for key in report_person_checker[id].keys():
            if report_counter[key] >= k:
                answer[i] += 1
    return answer



