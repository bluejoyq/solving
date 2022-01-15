
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

print(better_get_partial_match("ABABCABE"))
