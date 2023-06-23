import sys
from collections import deque

r, c = map(int,sys.stdin.readline().split())
mapp = []
adds = list('.'*(c+2))
mapp.append(adds)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

q = deque()
change = []
for i in range(r):
    mapp.append(list('.'+sys.stdin.readline().rstrip()+'.'))
mapp.append(adds)
def bfs(a,b):
    cnt = 0
    q.append((a,b))

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<r+2 and 0<=ny<c+2 and mapp[nx][ny] == '.':
                cnt +=1

        if cnt >=3:
            change.append((x,y))


ans = []
for i in range(r+2):
    for j in range(c+2):
        if mapp[i][j] == 'X':
            bfs(i,j)

for i,j in change:
    mapp[i][j] = '.'

min_x = 10
max_x = -1
min_y = 10
max_y = -1

for i in range(1,r+1):
    for j in range(1,c+1):
        if mapp[i][j] == 'X':
            min_x = min(min_x,i)
            max_x = max(max_x,i)
            min_y = min(min_y,j)
            max_y = max(max_y,j)

for i in range(min_x,max_x+1):
    print(''.join(mapp[i][min_y:max_y+1]))



