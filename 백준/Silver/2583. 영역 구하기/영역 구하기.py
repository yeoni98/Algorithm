import sys
from collections import deque

m, n, k  = map(int,sys.stdin.readline().split())

square = [[0]*n for _ in range(m)]
for i in range(k):
    x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
    x1,y1 = y1,x1
    x2,y2 = y2,x2
    for j in range(x1,x2,1):
        for k in range(y1,y2,1):
            square[j][k] = 1

q = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False]*n for _ in range(m)]


def bfs(a,b):
    q.append((a,b))
    visited[a][b] = True
    cnt =1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<m and 0<=ny<n and square[nx][ny] == 0 and visited[nx][ny] == False:
                visited[nx][ny] = True
                q.append((nx,ny))
                cnt +=1
    return cnt
rst = []
for i in range(m):
    for j in range(n):
        if square[i][j] == 0 and visited[i][j] == False:
            rst.append(bfs(i,j))
answer = sorted(rst)
print(len(answer))
print(*answer)
