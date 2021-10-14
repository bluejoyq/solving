# 내가 푼 문제는 아니고, 남이 질문한 문제임!.
from collections import deque

num = int(input())
s=[ [-1]*(num+1) for i in range(num+1)]
s[1][0]=0
q = deque()
q.append((1,0))  #현재 화면에 띄워진 갯수(1)와 클립보드의 갯수(0) 입력 
while(q):
	x,c = q.popleft() # x는 화면 갯수 , c는 클립보드 갯수
	if x==num:    #결과 도출시 출력
		print(s[x][c])
		break
	dx = [c,0,-1]   # 현재 화면 갯수+클립보드 수, 클립보드에 저장, 화면 갯수 -1
	for i in range(3):
		nx = x + dx[i]
		if nx < 0 or nx > num:
			continue
		if s[nx][x] == -1 and i == 1:
			#dx가 0, 클립보드에 저장하는 경우
			# temp=c    
			# c=x    클립보드에 현재 화면 갯수 입력
			# s[nx][c]=s[x][temp]+1
			s[nx][x] = s[x][c] + 1
			q.append((nx,x))
		
		if s[nx][c] == -1 and i != 1:
			s[nx][c]=s[x][c]+1    
			q.append((nx,c))