import sys
from collections import deque

n = int(sys.stdin.readline())
p,c = map(int,sys.stdin.readline().split())
m = int(sys.stdin.readline())

r = [[] for _ in range(n+1)]
q = deque()
check = [0]*(n+1)

def bfs(node):
    q.append(node)
    while q:
        node = q.popleft()
        for n in r[node]:
            if check[n] == 0:
                check[n] = check[node] + 1
                q.append(n)



for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    r[x].append(y)
    r[y].append(x)
   

bfs(p)

if check[c] >0:
    print(check[c])
else:
    print(-1)