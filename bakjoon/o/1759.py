L,C = map(int, input().split())
s = input().split()
vowel = ['a', 'e', 'i', 'o', 'u']
candidates = [[] for i in range(6)] # 0 : 모음x, 1: 모음o
result = set([])
s.sort()

if s[0] in vowel:
    candidates[1].append(s[0])
else:
    candidates[0].append(s[0])
for i in range(1, C):
    cur = s[i]
    pos = cur in vowel
    for j in range(6- pos):
        max_j = len(candidates[j])
        for k in range(max_j):
            target = candidates[j][k]
            if len(target) == L or target[-1] == cur:
                continue
            nxt = target + cur
            candidates[j+pos].append(nxt)
    candidates[pos].append(cur)
for i in range(1, min(L -1, 6)):
    for val in candidates[i]:
        if len(val) == L:
            result.add(val)
if len(result):
    print('\n'.join((sorted(result))))