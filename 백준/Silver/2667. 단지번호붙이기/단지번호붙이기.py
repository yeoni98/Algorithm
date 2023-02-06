import sys
from collections import deque

n = int(sys.stdin.readline())
graph = []
result = []

for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().rstrip())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    que = deque()
    que.append((x,y))
    graph[x][y] = 0
    cnt =1
    while que:
        x,y = que.popleft()
        for i in range(4):
            nx = x +dx[i]
            ny = y +dy[i]

            if 0<= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                que.append((nx,ny))
                cnt +=1
    return cnt

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt = bfs(i,j)
            result.append(cnt)
result.sort()
print(len(result))
print(*result, sep='\n')
