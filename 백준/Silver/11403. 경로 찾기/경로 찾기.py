import sys

#플로이드-와샬 알고리즘

n = int(sys.stdin.readline())
graph =  [list(map(int,sys.stdin.readline().split()))for i in range(n)]
for i in range(n):
    for j in range(n):
        for k in range(n):
            if graph[j][i]==1 and graph[i][k]==1: #j-i의 경로가 있고 i-k의 경로가 있다면 j-k의 경로도 있다
                graph[j][k] = 1

for i in graph:
    print(*i)
