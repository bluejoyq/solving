import math
x1,y1 = map(int,input().split())
x2,y2 = map(int,input().split())
x3,y3 = map(int,input().split())

def getRadianFromX(v1,v2):
    v1x,v1y = v1
    v2x,v2y = v2

    cos = (v1x * v2x + v1y * v2y)/(math.sqrt(v1x**2 + v1y**2) * math.sqrt(v2x**2 + v2y**2))
    return math.acos(cos)
a = getRadianFromX((x2 - x1, y2-y1), (x3 - x1,y3 - y1))
# 같은 직선 상에 있다면

print(a)
