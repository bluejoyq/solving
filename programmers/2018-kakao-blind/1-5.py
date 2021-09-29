# 21분
# [1차] 뉴스 클러스터링 https://programmers.co.kr/learn/courses/30/lessons/17677
def solution(str1, str2):
    from math import floor
    str1_set = {}
    for i in range(len(str1) - 1):
        target = str1[i:i+2]
        if not target.isalpha():
            continue
        target.upper()
        try:
            str1_set[target.upper()] += 1
        except:
            str1_set[target.upper()] = 1
    str2_set = {}
    for i in range(len(str2) - 1):
        target = str2[i:i+2]
        if not target.isalpha() or target[0] == " " or target[1] == " ":
            continue
        
        try:
            str2_set[target.upper()] += 1
        except:
            str2_set[target.upper()] = 1
    
    answer = 0
    intersection = 0
    union = 0
    for key in str1_set.keys():
        try:
            intersection += max(str1_set[key],str2_set[key])
            union += min(str1_set[key],str2_set[key])
            del str2_set[key] 
        except:
            intersection += str1_set[key]
    for key in str2_set.keys():
        intersection += str2_set[key]
    if intersection == 0:
        return 65536
    return floor((union/ intersection)* 65536)