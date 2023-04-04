import sys
from collections import deque

n, l, r = map(int,sys.stdin.readline().split())
a = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(n):
    a.append(list(map(int, sys.stdin.readline().split())))

def BFS(i,j):
    q = deque()
    u = deque()
    q.append((i,j))
    u.append((i,j))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==False:
                if l<= abs(a[nx][ny]-a[x][y]) <=r:
                    visited[nx][ny]=True
                    q.append((nx,ny))
                    u.append((nx,ny))
    return u

rst = 0
while True:
    visited = [[False] * n for _ in range(n)]
    flag = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == False:
                visited[i][j] = True
                country = BFS(i,j)

                if len(country) >1:
                    flag = 1
                    people = sum(a[x][y] for x,y in country)//len(country)

                    for x, y in country:
                        a[x][y] = people

    if flag == 0:
        print(rst)
        break

    rst +=1