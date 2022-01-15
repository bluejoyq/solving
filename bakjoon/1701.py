query = input()
N = len(query)


def make_pi_with_start(start):
    begin = 1
    matched = 0
    pi = [0] * N
    while begin + matched + start < N:
        if query[matched + start] == query[begin + matched + start]:
            matched += 1
            pi[begin + matched - 1] = matched
        elif matched == 0:
            begin += 1
        else:
            begin += matched - pi[matched - 1]
            matched = pi[matched-1]
    return(max(pi))
result = 0
for i in range(N):
    result = max(result,make_pi_with_start(i))
print(result)