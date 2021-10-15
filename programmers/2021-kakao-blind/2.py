def solution(orders, course):
	from itertools import combinations 
	answer = []
	for c in course:
		course_counter = {}
		for order in orders:
			menus = sorted(list(order))
			for course_menu in combinations(menus, c):
				course_menu = ''.join(course_menu)
				try:
					course_counter[course_menu] += 1
				except:
					course_counter[course_menu] = 1
		try:
			famous_course_value = max(course_counter.values())
			if famous_course_value < 2:
				break
			for k in course_counter.keys():
				if course_counter[k] == famous_course_value:
					answer.append(k)

		except:
			pass
			
	
	return sorted(answer)