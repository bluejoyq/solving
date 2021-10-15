from bisect import bisect_left
def solution(info, query):
	# 내가 생각하는 포인트 : 일단 점수들은 정렬되어 있어야함.
	# 24개를 걍 딕셔너리로 하고 각각의 조건에 해당하는 거를 리스트에 담아두자.
	# 이거 조건이 좀 빡씨네
	start = {}
	answer = []
	for one_info in info:
		cur =start
		details = one_info.split()
		
		for detail in details[:-1]:
			try:
				cur = cur[detail]
			except:
				cur[detail] = {}
				cur = cur[detail]
		try:
			cur['values'].append(int(details[-1]))
		except:
			cur['values'] = [int(details[-1])]
	

	next_possibles = [start]
	for i in range(4):
		possibles = next_possibles
		next_possibles = []
		while possibles:	
			cur = possibles.pop()
			for nxt in cur.keys():
				next_possibles.append(cur[nxt])
	for next_possible in next_possibles:
		next_possible['values'].sort()
	# q 처리
	for q in query:
		next_possibles = [start]
		
		query_details = list(q.split(' and '))
		for i in range(3):
			possibles = next_possibles
			next_possibles = []
			while possibles:
				cur = possibles.pop()
				if query_details[i] == '-':
					for nxt in cur.values():
						next_possibles.append(nxt) 
					continue
				try:
					next_possibles.append(cur[query_details[i]])
				except:
					pass	
		last_detail, score_detail = query_details[3].split()
		score_detail = int(score_detail)
		high_count = 0
		possibles = next_possibles
		next_possibles = []
		while possibles:
			cur = possibles.pop()
			if last_detail == '-':
				for nxt in cur.values():
					high_count += len(nxt['values']) - bisect_left(nxt['values'], score_detail)
				continue
			try:
				high_count += len(cur[last_detail]['values']) - bisect_left(cur[last_detail]['values'], score_detail)

			except:
				pass
		answer.append(high_count)
	return answer
