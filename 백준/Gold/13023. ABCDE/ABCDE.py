import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())
q = deque()
graph = [[] for i in range(n+1)]
visited = [False]*(n+1)
arrive = False

for i in range(m):
    a, b = map(int,sys.stdin.readline().split())
    graph[b].append(a)
    graph[a].append(b)


def DFS(start, depth):
    global arrive
    visited[start] = True
    if depth ==5:
        arrive = True
        return

    for i in graph[start]:
        if not visited[i]:
            DFS(i,depth+1)
            visited[i] = False
    visited[start] = False


for i in range(n):
    DFS(i,1)
    if arrive:
        break

if arrive:
    print(1)
else:
    print(0)
