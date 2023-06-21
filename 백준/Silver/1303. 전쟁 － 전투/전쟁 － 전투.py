import sys
from collections import deque


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def wbfs(a,b):
    q = deque()
    q.append((a,b))
    visited[a][b] = True
    N = 0
    while q:
        x, y = q.popleft()
        N+=1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and war[nx][ny] == 'W' and visited[nx][ny] == False:
                visited[nx][ny] = True
                q.append((nx, ny))
    return N

def bbfs(a,b):
    q = deque()
    q.append((a,b))
    visited[a][b] = True
    N = 0
    while q:
        x, y = q.popleft()
        N += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and war[nx][ny] == 'B' and visited[nx][ny] == False:
                visited[nx][ny] = True
                q.append((nx, ny))

    return N


n, m = map(int, sys.stdin.readline().split())
war = []
visited = [[False]*n for _ in range(m)]
white, blue = 0, 0

for i in range(m):
    war.append(list(sys.stdin.readline().rstrip()))

for i in range(m):
    for j in range(n):
        if war[i][j] == 'W' and visited[i][j] == False:
            N = wbfs(i,j)
            white += N*N
        if war[i][j] == 'B' and visited[i][j] == False:
            N = bbfs(i,j)
            blue += N*N


print(white,blue)