import sys
from collections import deque

n, m = map(int,sys.stdin.readline().split())
q = deque()
graph = [[] for i in range(n+1)]

for i in range(m):
    a, b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


def BFS(start):
    q = deque([start])
    visited[start] = True
    while q:
        x = q.popleft()
        for i in graph[x]:
            if not visited[i]:
                visited[i] = True
                q.append(i)

cnt = 0
visited = [False]*(n+1)

for i in range(1,n+1):
    if not visited[i]:
        if not graph[i]:
            visited[i] = True
            cnt +=1
        else:
            BFS(i)
            cnt +=1

print(cnt)




