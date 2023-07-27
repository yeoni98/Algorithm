import sys
from collections import deque

def bfs():
    q = deque()
    q.append((hx,hy))
    while q:
        dx, dy = q.popleft()
        if abs(fx-dx) + abs(fy-dy) <=1000:
            return "happy"
        for _ in range(n):
            if not visited[_]:
                nx, ny = c[_]
                if abs(nx- dx) + abs(ny-dy) <=1000:
                    visited[_] = True
                    q.append((nx,ny))
    return "sad"





t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    hx, hy = map(int,sys.stdin.readline().split())
    c = []
    for j in range(n):
        x, y = map(int, sys.stdin.readline().split())
        c.append((x,y))
    fx, fy = map(int,sys.stdin.readline().split())
    visited = [False for _ in range(n+1)]
    print(bfs())






