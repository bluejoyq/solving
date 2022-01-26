N = int(input())

a_values = list(map(int,input().split()))
b_values = list(map(int, input().split()))
a_values.sort()
b_values.sort()
a_values_differ = [abs(a_values[i + 1] - a_values[i]) for i in range(N - 1)]
a_values_differ.append(360000 + a_values[0] - a_values[-1])
b_values_differ = [abs(b_values[i + 1] - b_values[i]) for i in range(N - 1)]
b_values_differ.append(360000 + b_values[0] - b_values[-1])

# 어디서부터 비교할지 시작 지점을 찾고, 거기서부터 같은지 비교
# 비교할 대상 문자열을 2배로 늘리고 pi제작

pi = [0] * N
begin = 1
matched = 0
while begin + matched < N:
    if a_values_differ[(begin + matched)] == a_values_differ[matched]:
        matched += 1
        pi[(begin + matched - 1)] = matched
    elif matched == 0:
        begin += 1
    else:
        begin += matched - pi[(matched - 1)]
        matched = pi[(matched - 1)]


start = 0
matched = 0
while start + matched < N * 2 and matched < N:
    if a_values_differ[(matched) ] == b_values_differ[(start + matched) % N]:
        matched += 1
    elif matched == 0:
        start += 1
    else:
        start += matched - pi[(matched - 1)]
        matched = pi[(matched - 1)]

if matched == N:
    print("possible")
else:
    print("impossible")