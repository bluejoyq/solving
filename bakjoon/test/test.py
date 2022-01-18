a = [1, 1, 1, 2, 2]
b = int(input())
for i in range(b):
    num = int(input())
    if num > 5:
        while len(a) < num:
            a.append(a[len(a) - 1] + a[len(a) - 5])
        print(a[len(a) - 1])
    else:
        print(a[num - 1])

def rec_tri(M):
    mry = [0] * 101
    if mry[M]:
        return mry[M]
    func_result = 0
    if M < 6:
        ex = [0,1,1,1,2,2]
        func_result = ex[M]
    else:
        func_result = rec_tri(M-1) + rec_tri(M-5)
    mry[M] = func_result
    return func_result

