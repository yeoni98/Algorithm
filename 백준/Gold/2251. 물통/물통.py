import sys
from collections import deque

a, b, c = map(int,sys.stdin.readline().split())

visited = [[False]*(b+1) for _ in range(a+1)]
ans = []
q = deque()
q.append((0,0))

def pour(i,j):
    if visited[i][j] == False:
        visited[i][j] = True
        q.append((i,j))

def bfs():
    while q:
        x,y = q.popleft()
        z = c-x-y
        if x == 0:
            ans.append(z)

        # a->b
        water = min(x, b - y)
        pour(x - water, y + water)
        # a->c
        water = min(x, c - z)
        pour(x - water, y)

        # b->a
        water = min(y, a - x)
        pour(x+water, y-water)
        #b->c
        water = min(y, c-z)
        pour(x,y-water)

        #c->a
        water = min(z, a - x)
        pour(x+water, y)
        #c->b
        water = min(z, b-y)
        pour(x,y+water)
bfs()
answer = sorted(set(ans))
print(*answer)