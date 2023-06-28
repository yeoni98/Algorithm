import sys
from collections import deque

n, k = map(int,sys.stdin.readline().split())
graph = [0]*100001
visited = [False]*100001
q = deque()
q.append(n)
ans = 0
cnt = 0
while q:

    x = q.popleft()
    if x==k:
        cnt +=1
        ans = graph[x]
        continue

    for nx in (x-1,x+1,x*2):
        if 0<=nx<=100000 and (visited[nx] == False or graph[nx] == graph[x]+1):
            graph[nx] = graph[x] + 1
            q.append(nx)
            visited[nx] = True


print(ans)
print(cnt)
