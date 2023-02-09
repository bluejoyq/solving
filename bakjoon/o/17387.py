def ccw(p1,p2, p3):
    s = p1[0] * p2[1] + p2[0] * p3[1]+ p3[0] * p1[1]
    s -= p1[1] * p2[0] + p2[1] * p3[0] + p3[1] * p1[0]
    if s > 0:
        return 1
    elif s==0:
        return 0
    return -1


def is_intercept(l1,l2):
    p1 = tuple(l1[0:2])
    p2 = tuple(l1[2:])
    p3 = tuple(l2[0:2])
    p4 = tuple(l2[2:])

    p1_p2 = ccw(p1,p2,p3) * ccw(p1,p2,p4)
    p3_p4 = ccw(p3,p4,p1) * ccw(p3,p4,p2)

    if p1_p2 == 0 and p3_p4  == 0:
        if p1 > p2:
            p2,p1 = p1, p2
        if p3 > p4:
            p3, p4 = p4 , p3
        return p3 <= p2 and p1 <= p4
    return p1_p2 <= 0 and p3_p4 <= 0

l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))

print(int(is_intercept(l1,l2)))