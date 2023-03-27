import sys
sys.setrecursionlimit(100000)
n = int(sys.stdin.readline())
graph = []
ans = 1
max_num = 0
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(x,y,num):
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if 0<=nx<n and 0<=ny<n and visited[nx][ny]==0 and graph[nx][ny]>num:
            visited[nx][ny] = 1
            dfs(nx,ny,num)

for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))
    for j in graph[i]:
        if j>max_num:
            max_num = j

for i in range(max_num):
    visited = [[0] * n for _ in range(n)]
    cnt = 0
    for j in range(n):
        for k in range(n):
            if graph[j][k]>i and visited[j][k]==0:
                cnt +=1
                visited[j][k] = 1
                dfs(j,k,i)
    ans = max(cnt, ans)

print(ans)
