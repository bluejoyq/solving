# https://programmers.co.kr/learn/courses/30/lessons/77484?language=python3

def solution(lottos, win_nums):
	ranks_by_correct = [6,6,5,4,3,2,1]
	original_correct = 0
	wrong_count = 0
	for lotto in lottos:
		if lotto == 0:
			wrong_count += 1
			continue
		try:
			idx = win_nums.index(lotto)
		except:
			continue
		original_correct += 1
		win_nums[idx] = 0
   

	return [ranks_by_correct[original_correct], 
			ranks_by_correct[original_correct + wrong_count]]