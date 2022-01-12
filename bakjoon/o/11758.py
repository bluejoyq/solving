x1,y1 = map(int,input().split())
x2,y2 = map(int,input().split())
x3,y3 = map(int,input().split())

def get_vector(x1,y1,x2,y2):
    return [x1-x2, y1-y2]

def get_cross_product(v1,v2):
    x1,y1 = v1
    x2,y2 = v2

    return x1*y2 - x2*y1

v1 = get_vector(x1,y1,x2,y2)
v2 = get_vector(x1,y1,x3,y3)
sin_theta = get_cross_product(v1,v2)
if abs(sin_theta) < 1e-6:
    print(0)
elif sin_theta < 0:
    print(-1)
else:
    print(1)