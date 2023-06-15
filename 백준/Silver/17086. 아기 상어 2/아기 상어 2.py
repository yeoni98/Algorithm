import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split(' '))
q = []
shark = deque()

for i in range(n):
    a = list(map(int,sys.stdin.readline().split()))
    q.append(a)
    for j in range(m):
        if a[j] == 1:
            shark.append((i,j))

dx = [-1, -1, -1, 0, 1, 0, 1, 1]
dy = [-1, 0, 1, 1, 1, -1, 0, -1]
cnt = 0
def bfs():
    global cnt
    while shark:
        x, y = shark.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m and q[nx][ny] == 0:
                shark.append((nx,ny))
                q[nx][ny] = q[x][y]+1
                cnt = max(cnt,q[nx][ny])


bfs()

print(cnt-1)