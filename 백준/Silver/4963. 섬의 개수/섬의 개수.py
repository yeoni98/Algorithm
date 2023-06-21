import sys
from collections import deque


dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]


def bfs(a,b):
    q = deque()
    q.append((a,b))
    visited[a][b] = True
    while q:
        x, y = q.popleft()

        for n in range(8):
            nx = x + dx[n]
            ny = y + dy[n]

            if 0 <= nx < h and 0 <= ny < w and maps[nx][ny] == 1 and visited[nx][ny] == False:
                visited[nx][ny] = True
                q.append((nx, ny))


while True:
    w, h = map(int,sys.stdin.readline().split())
    if w == 0 and h == 0:
        break
    maps = []
    visited = [[False]*w for _ in range(h)]
    cnt = 0

    for i in range(h):
        maps.append(list(map(int,sys.stdin.readline().split())))

    for i in range(h):
        for j in range(w):
            if maps[i][j] == 1 and visited[i][j] == False:
                bfs(i,j)
                cnt +=1
    print(cnt)