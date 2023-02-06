import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())
graph = []
que = deque()

dx = [-1,1,0,0]
dy = [0,0,-1,1]
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

def bfs():
    while que:
        x,y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] +1
                que.append((nx,ny))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            que.append((i,j))
           


bfs()

flag = 0
result = -2

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            flag = 1
        result = max(result,graph[i][j])

if flag == 1:
    print(-1)
elif result == 1:
    print(0)
else:
    print(result - 1)