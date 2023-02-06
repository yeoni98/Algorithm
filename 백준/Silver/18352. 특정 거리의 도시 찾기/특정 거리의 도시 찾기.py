import heapq
import sys

INF = int(1e9)


n, m, k, x = map(int,sys.stdin.readline().split())
graph = [[] for i in range(n+1)]
distance = [INF] *(n+1)

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append((b,1))

def dijkstra(x):
    que = []
    heapq.heappush(que,(0,x))
    distance[x] = 0
    while que:
        dist, now = heapq.heappop(que)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost <distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(que,(cost,i[0]))

dijkstra(x)


none = 1

for i in range(1,n+1):
    if distance[i] == k:
        none = 0
        print(i)

if none:
    print(-1)