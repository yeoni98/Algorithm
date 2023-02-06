import sys
sys.setrecursionlimit(10**9)

n = int(sys.stdin.readline())
graph = [[] for i in range(n+1)]
ans = [[] for i in range(n+1)]
visited = [False]*(n+1)
for i in range(n-1):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(node):
    visited[node] = True
    for x in graph[node]:
        if not visited[x]:
            dfs(x)
            ans[x] = node

dfs(1)
for x in range(2,n+1):
    print(ans[x])
