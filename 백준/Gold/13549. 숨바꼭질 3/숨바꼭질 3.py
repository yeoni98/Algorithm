import sys
from collections import deque

n, k = map(int,sys.stdin.readline().split())
visited = [False]*100001
graph = [0]*100001
q = deque()
q.append(n)
while q:
    x = q.popleft()

    if x == k:
        print(graph[x])
        break
    for nx in (x-1,x+1,x*2):
        if 0<=nx<=100000 and visited[nx] == False and graph[nx] ==0:

            if nx == x*2:
                graph[nx] = graph[x]
                q.appendleft(nx)
            #     순간이동 했을 때 소요되는 시간이 0초 이므로 우선순위 반영을 위해 appendleft를 쓴다.
            else:
                graph[nx] = graph[x]+1
                q.append(nx)
            visited[nx] = True