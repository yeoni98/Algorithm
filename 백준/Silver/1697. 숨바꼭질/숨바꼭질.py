import sys
from collections import deque
n,k = map(int,sys.stdin.readline().split())
graph = [0]*100001

def bfs():
    que = deque()
    que.append(n)

    while que:
        x = que.popleft()
        if x == k:
            print(graph[x])
            break
        for nx in (x-1,x+1,x*2):
            if 0<=nx<=100000 and graph[nx]==0:
                graph[nx] = graph[x] +1
                que.append(nx)
bfs()
