import sys
from collections import deque

r, c, n = map(int,sys.stdin.readline().split())
graph = []


for i in range(r):
    graph.append(list(map(str, sys.stdin.readline().rstrip())))
#초기 상태~1초 후
def loc_bomb():
    for i in range(r):
        for j in range(c):
            if graph[i][j] == "O":
                que.append((i,j))
#2초 후 . 을 O으로(폭탄 설치)
def full_bomb():
    for i in range(r):
        for j in range(c):
            if graph[i][j] != "O":
                graph[i][j] = "O"
#3초 후 폭발
def bombs():
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while que:
        x, y = que.popleft()
        graph[x][y] = "."

        for i in range(4):
            nx = x +dx[i]
            ny = y +dy[i]

            if 0<= nx < r and 0<= ny < c and graph[nx][ny]  == "O":
                graph[nx][ny] = "."
#초기-1초 후
n-=1
while n:
    que = deque()
    loc_bomb()
    #2초 후
    full_bomb()
    n-=1

    if n == 0:
        break
    #3초 후
    bombs()
    n-=1

for i in range(r):
    print("".join(graph[i]))