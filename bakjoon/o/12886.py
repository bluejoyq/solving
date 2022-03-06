def solve():
    A,B,C = map(int, input().split())


    cache = [[{} for i in range(1000)] for j in range(1000)]

    findings = [(A,B,C)]
    cache[A][B][C] = 1


    def valid_check_and_do(a,b,c):
        try:
            cache[a][b][c]
            return 0
        except:
            cache[a][b][c] = 1
            findings.append((a,b,c))
            return 1
    while findings:
        a,b,c = findings.pop()
        if a == b and b == c:
            return 1


        if a <= b and 2 * a < 1000:
            valid_check_and_do(2 * a, b-a,c)
        if a <= c and 2 * a < 1000:
            valid_check_and_do(2 * a, b,c - a)
        if b <= a and 2 * b < 1000:
            valid_check_and_do(a - b, 2 * b,c)
        if b <= c and 2 * b < 1000:
            valid_check_and_do(a, 2 * b,c - b)  
        if c <= a and 2 * c < 1000:
            valid_check_and_do(a - c, b,2 * c)  
        if c <= b and 2 * c < 1000:
            valid_check_and_do(a, b - c,2 *c)  



    return 0

print(solve())