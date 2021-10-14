import sys
input = sys.stdin.readline
def prime(a):
  if a == 1:
    return False
  else:
    for i in range(2,int(a**(0.5)+1)):
      if a % i == 0:
        return False
    else:
      return True

num =[]
for i in range(2,10001):
  if prime(i):
    num.append(i)
print(len(num))
n = int(input())
list = []
for i in range(n):
  a = int(input())
  if prime(a//2):
    print(a//2,a//2)
  else:
    for j in range(2,(a//2)):
      if j in num:
        if (a-j) in num:
          list.append(j)
    print(list[-1],a-list[-1])
    list = []
