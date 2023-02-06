import sys
from collections import deque

m, n, h = map(int, sys.stdin.readline().split())
graph = [[list(map(int,sys.stdin.readline().split()))for i in range(n)]for i in range(h)]
que = deque()

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                que.append((i,j,k))



def bfs():
    while que:
        z,x,y = que.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0<=nx<n and 0<=ny<m and 0<=nz<h and graph[nz][nx][ny] == 0:
                graph[nz][nx][ny] = graph[z][x][y] +1
                que.append((nz,nx,ny))




bfs()

flag = 0
result = -2

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 0:
                flag = 1
            result = max(result, graph[i][j][k])

if flag == 1:
    print(-1)
elif result == 1:
    print(0)
else:
    print(result - 1)