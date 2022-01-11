import math
x1,y1 = map(int,input().split())
x2,y2 = map(int,input().split())
x3,y3 = map(int,input().split())

# 거리가 총 3개죠? 3개의 거리가 일차 결합이면 일직선상에 있다.
def get_distance(x1,y1,x2,y2):
    return (abs(x1-x2)**2 + abs(y1-y2)**2)**0.5

v1 = get_distance(x1,y1,x2,y2)
v2 = get_distance(x2,y2,x3,y3)
v3 = get_distance(x3,y3,x1,x2)
if sum(v1,v2,v3) - 2 * max(v1,v2,v3) < 1e6:
