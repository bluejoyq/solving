# 25분 여기까지 103분 
# [1차] 프렌즈4블록 https://programmers.co.kr/learn/courses/30/lessons/17679
def solution(m, n, board):
    # 높이가 m
    # 4개짜리 틀로 쭉 봐야할듯
    # 최대 900칸을 본다면 4* 30 * 30 약 한번 체크에 3600개
    # 이정도는 감당 가능
    # 다 찾은 다음에는 구간 del? 0으로 갱신하는 프로세스를 한번 거치자
    board = [list(b) for b in board]
    def check():
        del_list = set([])
        for r in range(m- 1):
            for c in range(n - 1):
                # 너무 하드코딩인데;
                if board[r][c] != "0" and board[r][c] == board[r + 1][c] == board[r][c+1] == board[r+1][c+1]:
                    del_list.add((r,c))
                    del_list.add((r + 1,c))
                    del_list.add((r,c + 1))
                    del_list.add((r + 1,c + 1))
        return del_list
    def deleting(del_list):
        for r,c in del_list:
            board[r][c] = "0"
    
    def update():
        for c in range(n):
        
            new_row = ["0"] * m
            cur = m- 1
            for r in range(m -1, -1, -1):
                if board[r][c] == "0":
                    continue

                new_row[cur] = board[r][c]
                cur -= 1
            
            for r in range(m):
                board[r][c] = new_row[r]
                
    answer = 0
    del_list = check()
    while del_list:
        answer += len(del_list)
        deleting(del_list)
        update()
        del_list = check()
        
    return answer
print(solution(4,	5,	["CCBDE", "AAADE", "AAABF", "CCBBF"]))