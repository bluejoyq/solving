l1 = map(int,input().split())
l2 = map(int,input().split())
MAX = 9876543210
def getSlope(two_points):
    x1,y1,x2,y2 = two_points

    if y1 == y2:
        return MAX
    return (y2-y1) / (x2 - x1)

s1 = getSlope(l1)
s2 = getSlope(l2)

if abs(abs(s1) - abs(s2)) < 1e9:
    print(0)
else:
    print(1)