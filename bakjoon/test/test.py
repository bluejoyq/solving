import random


while True: 
    target =random.uniform(1,2)
    a = str(round(target,2))
    b = format(target,".2f")
    if a != b:
        print(target,a,b)
        break