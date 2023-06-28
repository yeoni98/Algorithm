import sys
from collections import deque
n, m = map(int,sys.stdin.readline().split())
paper = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited = [[False]*m for _ in range(n)]
ans = []

for i in range(n):
    paper.append(list(map(int,sys.stdin.readline().split())))

def bfs(a,b):
    q = deque()
    cnt = 1
    q.append((a,b))
    visited[a][b] = True
    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m:
                if visited[nx][ny]== False and paper[nx][ny] ==1:
                    cnt += 1
                    visited[nx][ny] = True
                    q.append((nx, ny))

    return cnt

for i in range(n):
    for j in range(m):
        if visited[i][j] == False and paper[i][j] == 1:
            ans.append(bfs(i,j))

if len(ans) >=1:
    print(len(ans))
    print(max(ans))
else:
    print(0)
    print(0)


