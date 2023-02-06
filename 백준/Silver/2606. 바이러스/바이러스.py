n = int(input())
connect = int(input())

graph = [[] for i in range(n+1)]
visited = [0]*(n+1)

for i in range(connect):
    a,b = map(int,input().split())
    graph[a] += [b]
    graph[b] += [a]

def dfs(connect):
    visited[connect] = 1
    for x in graph[connect] :
        if visited[x] == 0:
            dfs(x)

dfs(1)
print(sum(visited)-1)