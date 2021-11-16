def solution(leave, day, holidays):
	is_day_free = [0] * 32
	first_weekend_by_day = {
		'MON': 5,
		'TUE': 4,
		'WED': 3,
		'THU': 2,
		'FRI': 1,
		'SAT': 0,
		'SUN':6
	}

	for holiday in holidays:
		is_day_free[holiday] = 1

	rest_day = first_weekend_by_day[day]
	if rest_day == 6:
		is_day_free[1] = 1
	
	for weekend in range(1 + rest_day,31,7):
		is_day_free[weekend] = 1
		is_day_free[weekend + 1] = 1

	findings = []
	answer = -1
	# used_leave, cur_day, cur_holiday_long
	for day_idx in range(1,30):
		if is_day_free[day_idx]:
			findings.append((0,day_idx + 1, 1))
		else:
			findings.append((1, day_idx + 1, 1))
	
	while findings:
		used_leave, cur_day, cur_holiday_long = findings.pop()
		if cur_day == 31:
			answer = max(answer, cur_holiday_long)
			continue

		if is_day_free[cur_day]:
			findings.append((used_leave,cur_day + 1, cur_holiday_long + 1))
			continue

		if used_leave == leave:
			answer = max(answer, cur_holiday_long)
			continue

		findings.append((used_leave + 1,cur_day + 1, cur_holiday_long + 1))
	return answer
