def solution(n, k):
    import re
    str_n = ""
    q, r = divmod(n, k)
    str_n+= str(r)
    while q != 0:
        q, r = divmod(q, k)
        str_n+= str(r)
    str_n = str_n[::-1]
    
    max_range = 10000000
    answer = 0
    for num in re.split('0{1,}',str_n):
        if num == "" or num == "1":
            continue
        num = int(num)
        passed = True
        for i in range(2,int(num **0.5) + 1):
            if num % i ==0:
                passed = False
                break
            
        if passed:
            answer += 1
    return answer