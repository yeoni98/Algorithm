import sys
from collections import deque

n = int(sys.stdin.readline()) #n*n
k = int(sys.stdin.readline())
board = [[0]*n for _ in range(n)]
for i in range(k):
    a, b = map(int,sys.stdin.readline().split())
    board[a-1][b-1] = 1
l = int(sys.stdin.readline())
time_dict = {}
for i in range(l):
    X,c = sys.stdin.readline().split()
    time_dict[int(X)] = c

dx = [0,1,0,-1]
dy = [1,0,-1,0]

x,y,d = 0,0,0

snake = deque([])
time = 0
while True:
    snake.append((x,y))
    time += 1

    x+=dx[d]
    y+=dy[d]
    if 0>x or x>=n or 0>y or y>=n or board[x][y] == 2:
        break
    if not board[x][y]:
        i, j = snake.popleft()
        board[i][j] = 0
    board[x][y] = 2

    if time in time_dict:
        if time_dict[time] =='D':
            d= (d+1)%4
        else:
            d = (d-1)%4

print(time)


# 0 0 0 0 0 0
# 0 0 0 0 1 0
# 0 0 0 1 0 0
# 0 0 0 0 0 0
# 0 0 1 0 0 0
# 0 0 0 0 0 0
# // 회전 할 때 1초 소요
#
# 0 1 1 1 1 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0