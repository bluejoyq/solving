tmp = []
while True:
    try:
        a = list(reversed(input().split()))
        print(a)
        tmp.append([int(a[0]), a[1]])
    except:
        break

tmp.sort()
print(len(tmp))
for i in range(len(tmp)):
    if tmp[i][0] == 22:
        print(i)
        break