def displayPathtoPrincess(n,grid):
	princess = []
	me = []
	for r in range(n):
		for c in range(n):
			if grid[r][c] == 'm':
				me = [r,c]
			if grid[r][c] == 'p':
				princess = [r,c]
	col_gap = me[0] - princess[0]
	row_gap = me[1] - princess[1]
	if col_gap > 0:
		for i in range(abs(col_gap)):
			print('UP')
	else:
		for i in range(abs(col_gap)):
			print('DOWN')
	if row_gap > 0:
		for i in range(abs(row_gap)):
			print('LEFT')
	else:
		for i in range(abs(row_gap)):
			print('RIGHT')
displayPathtoPrincess(3, [['-','-','-'], ['-','m','-'],['p','-','-']])
'''
m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)
'''