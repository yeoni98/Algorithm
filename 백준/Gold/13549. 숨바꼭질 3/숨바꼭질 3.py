import sys
from collections import deque

n, k = map(int,sys.stdin.readline().split())
graph = [0]*100001
visited = [False]*100001
q = deque()
q.append(n)
while q:
    x = q.popleft()
    if x==k:
        print(graph[x])
        break
    for nx in (x-1,x+1,x*2):
        if 0<=nx<=100000 and visited[nx] == False:
            if nx == x*2:
                graph[nx] = graph[x]
                q.appendleft(nx)
            else:
                graph[nx] = graph[x] + 1
                q.append(nx)
            visited[nx] = True



