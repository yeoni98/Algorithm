import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

def bfs():
    graph = [0] * 100001
    graph[n] = 1
    que = deque([n])

    while que:
        target = que.popleft()
        if target == k:
            return graph[target]
        for i in (target +1, target -1, target*2):
            if 0<= i <=100000 and graph[i] == 0:
                if i == target*2:
                    graph[i] = graph[target]
                    que.appendleft(i)
                else:
                    graph[i] = graph[target] + 1
                    que.append(i)

print(bfs()-1)