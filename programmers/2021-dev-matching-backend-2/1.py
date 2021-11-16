def solution(registered_list, new_id):
	answer = ''
	id_mem = {}
	for registered_id in registered_list:
		id_mem[registered_id] = 1

	try:
		id_mem[new_id]
	except:
		return new_id
	
	num_location = len(new_id)
	for i in range(len(new_id)):
		char = new_id[i]
		try:
			int(char)
			num_location = i
			break
		except:
			continue
	
	S = new_id[:num_location]
	if num_location == len(new_id):
		N = 1
	else:
		N = int(new_id[num_location:])

	while(id_mem.get(S + str(N)) != None):
		N += 1
	

	return S + str(N)