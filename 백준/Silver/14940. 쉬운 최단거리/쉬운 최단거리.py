import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = []
visited = []

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

visited = [[0 for i in range(m)] for j in range(n)]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            x, y = i,j
            break


dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    que = deque()
    que.append((x,y))
    graph[x][y] = 0
    visited[x][y] = 1


    while que:
        x,y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] =1
                que.append((nx,ny))
                graph[nx][ny] = graph[x][y] + 1



bfs(x,y)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j] == 0:
            graph [i][j] = -1


for i in range(n):
    print(*graph[i])