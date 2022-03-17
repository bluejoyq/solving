import sys
input = sys.stdin.readline
def check_two(edges,checkings,i):
  findings = [i]
  while findings:
    cur = findings.pop()
    if not checkings[cur]: 
      checkings[cur] = 1
    for key in edges[cur].keys():
      if not checkings[key]:
        findings.append(key)
      if checkings[cur] ==checkings[key]:
        return 0  
      else:
        checkings[key] = -checkings[cur]
      
      
  return 1
K = int(input())

for _ in range(K):
  V, E = map(int, input().split())
  edges = [{} for i in range(V + 1)]
  for i in range(E):
    a,b = map(int, input().split())
    edges[a][b] = 1 
    edges[b][a] = 1
  
  checkings = [0] * (V+1)
  check = 1
  
  for i in range(1, V+1):
    if not check_two(edges,checkings,i):
      check = 0
      break
  if check:
    print("YES")
  else:
    print("NO")