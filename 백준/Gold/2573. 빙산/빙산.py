import sys
from collections import deque
n, m = map(int,sys.stdin.readline().split())
arctic = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]

q = deque()
year = 0
check = False

for i in range(n):
    iceberg = list(map(int,sys.stdin.readline().split()))
    arctic.append(iceberg)

def bfs(a,b):
    q.append((a,b))
    while q:
        x,y = q.popleft()
        visited[x][y] = True
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<n and 0<=ny<m and visited[nx][ny] == False:
                if arctic[nx][ny] !=0:
                    visited[nx][ny] = True
                    q.append((nx,ny))
                else:
                    cnt[x][y] +=1
    return 1

while True:

    visited = [[False] * m for _ in range(n)]
    cnt = [[0] * m for _ in range(n)]
    result = []
    for i in range(n):
        for j in range(m):
            if arctic[i][j] !=0 and visited[i][j] == False:
                result.append(bfs(i,j))
    for i in range(n):
        for j in range(m):
            arctic[i][j] -= cnt[i][j]
            if arctic[i][j] < 0:
                arctic[i][j] = 0
    if len(result) == 0:
        break
    if len(result) >=2:
        check = True
        break
    year +=1


if check:
    print(year)
else:
    print(0)