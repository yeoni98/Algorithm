import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [[] for i in range(n+1)]


for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[b] += [a]

def bfs(start):
    q = deque()
    q.append(start)
    visited = [0] * (n + 1)
    visited[start] = 1
    cnt = 1
    while q:
        x = q.popleft()
        for i in graph[x]:
            if visited[i] == 0:
                cnt+=1
                visited[i] = 1    
                q.append(i)
    return cnt

max_cnt = 0
result = []
for i in range(1,n+1):
    tmp = bfs(i)
    if max_cnt == tmp:
        result.append(i)
    if max_cnt <tmp:
        max_cnt = tmp
        result = []
        result.append(i)


print(*result)
