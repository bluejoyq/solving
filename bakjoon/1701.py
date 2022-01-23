
def solve(query):


    def better_get_partial_match(N):
        M = len(N)
        pi = [0] * M
        
        begin = 1
        matched = 0
        while begin + matched < M:
            if N[begin + matched] == N[matched]:
                matched += 1
                pi[begin + matched - 1] = matched
            elif matched == 0: 
                begin += 1
            else:
                begin += matched - pi[matched - 1]
                matched = pi[matched - 1]
        return pi


    pi = better_get_partial_match(query)
    print(pi)
    print(max(pi))
    return max(pi)

#query = input()
try:
    assert(solve('ababeabe') == 3)

except Exception as err:
    print(err)