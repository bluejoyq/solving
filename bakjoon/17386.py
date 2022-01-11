points_l1 = list(map(int,input().split()))
points_l2 = list(map(int,input().split()))
MAX = 9876543210

class Line:
    def __init__(self, p1,p2):
        x1,y1 = p1
        x2,y2 = p2
        if y1 == y2:
            self.slope = MAX
        else:
            self.slope =  (y2-y1) / (x2 - x1)
        self.c_num = y1 - self.slope * x1
    def get_slope(self):
        return self.slope
    def get_y(self, x):
        return self.slope * x + self.c_num 



l1 = Line(points_l1[:2], points_l1[2:])
l2 = Line(points_l2[:2], points_l2[2:])
# 평행하면 만나지 않는다.
if abs(l1.get_slope() - l2.get_slope()) < 1e9:
    print(0)
else:
