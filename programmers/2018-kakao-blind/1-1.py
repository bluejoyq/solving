# 약 5분
# [1차]비밀지도 https://programmers.co.kr/learn/courses/30/lessons/17681
def solution(n, arr1, arr2):
    def check(num,j):
        return num & (1 << j)
    answer = []
    for i in range(n):
        line = ""
        for j in range(n-1,-1,-1):
            if check(arr1[i], j) | check(arr2[i], j):
                line += "#"
            else:
                line += " "
        answer.append(line)
    
    return answer