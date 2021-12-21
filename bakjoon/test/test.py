N = str(input())

z = N.split('-')

for i in range(0, len(z)):
    j = list(z[i])
    while j[0] == '0':
        if len(j) == 1:
            break
        else:
            del j[0]
    h = ''
    for x in j:
        h += x
    z[i] = h
        
answer = eval(z[0])*2

for k in z:
    answer -= eval(k)

print(answer)
# 1010-10101+01010+0000