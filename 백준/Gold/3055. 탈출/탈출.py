import sys
from collections import deque

r, c = map(int,sys.stdin.readline().split())

map = [list(sys.stdin.readline().rstrip()) for i in range(r)]
distance = [[0]*c for i in range(r)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
q = deque()

def bfs(Dx, Dy):
    while q:
        x, y = q.popleft()
        if map[Dx][Dy] == 'S':
            return distance[Dx][Dy]
            break
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<r and 0<= ny<c:
                if(map[nx][ny] == '.' or map[nx][ny] == 'D') and map[x][y] =='S':
                    map[nx][ny] = 'S'
                    distance[nx][ny] = distance[x][y] +1
                    q.append((nx,ny))
                elif(map[nx][ny] == '.' or map[nx][ny] == 'S') and map[x][y] == '*':
                    map[nx][ny] = '*'
                    q.append((nx,ny))
    return "KAKTUS"

for x in range(r):
    for y in range(c):
        if map[x][y] == 'S':
            q.append((x,y))
        elif map[x][y] == 'D':
            Dx,Dy = x,y

for x in range(r):
    for y in range(c):
        if map[x][y] == '*':
            q.append((x,y))

print(bfs(Dx,Dy))


