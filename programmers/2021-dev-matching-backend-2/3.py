def solution(macarons):
	SIZE = 6
	board = [[0] * (SIZE) for i in range(SIZE)]
	four_search = [[0,1],[1,0],[0,-1],[-1,0]]
	
	def go_down(cur_r, cur_c,color):
		board[cur_r][cur_c] = 0
		while(cur_r < SIZE -1 and board[cur_r + 1][cur_c] == 0):
			cur_r += 1
		board[cur_r][cur_c] = color
		return cur_r, cur_c

	def find_near_same_color_macaron(r,c, color):
		visited = [[0] * (SIZE) for i in range(SIZE)]
		findings =[(r,c)]
		sames = [(r, c)]
		visited[r][c] = 1
		while findings:
			cur_r,cur_c = findings.pop()
			for search in four_search:
				new_r = search[0] + cur_r
				new_c = search[1] + cur_c
				if -1 < new_r < SIZE and -1 <new_c <SIZE and board[new_r][new_c] == color and visited[new_r][new_c] == 0:
					visited[new_r][new_c] = 1
					findings.append((new_r,new_c))
					sames.append((new_r,new_c))	
		return sames		

	def do_macaron_process(start_r,start_c,color):
		# 2 주변의 마카롱들 찾아서 좌표 리턴하기
		sames = find_near_same_color_macaron(start_r,start_c, color)

		
		if len(sames) < 3:
			return
		# 3 좌표 개수가 3 이상이라면 다 터트리기
		check_start_row_by_col = [-1] * SIZE
		for r,c in sames:
			board[r][c] = 0
			check_start_row_by_col[c] = max(check_start_row_by_col[c], r)

		# 4 터진거 위에 있는 마카롱에 대해서 이 함수 재귀 호출
		process_candidates = []
		for c in range(SIZE):
			for r in range(check_start_row_by_col[c], -1, -1):
				if board[r][c] == 0:
					continue
				nxt_r,nxt_c = go_down(r,c, board[r][c])
				process_candidates.append((nxt_r,nxt_c))
		for r,c in process_candidates:
			do_macaron_process(r,c,board[r][c])
	for macaron in macarons:
		pos, color = macaron
		
		# 1 갈 수 있을 만큼 아래로 움직이기
		new_r,new_c = go_down(0,pos-1, color)
		do_macaron_process(new_r,new_c, color)
	answer = ["".join(map(str,b)) for b in board]

	return answer