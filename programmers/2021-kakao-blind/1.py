from collections import deque
def solution(new_id):
	answer = deque([])
	new_id = new_id.lower()

	for letter in new_id:
		if letter.isalnum() or letter == '-' or letter == '_' or letter =='.':
			if len(answer) == 0:
				if letter != '.':
					answer.append(letter)
				continue
			elif answer[-1] == '.' and letter == '.':
				continue
			answer.append(letter)
	try:
		while(answer[-1] == '.'):
			answer.pop()
	except:
		pass
	if len(answer) == 0:
		answer.append('a')
	
	while(len(answer) > 15 or answer[-1] == '.'):
		answer.pop()

	while len(answer) < 3:
		answer.append(answer[-1])
		
	result = ""
	for char in answer:
		result += char
	return result