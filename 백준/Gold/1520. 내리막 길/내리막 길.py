import sys
sys.setrecursionlimit(10 ** 8)
m, n = map(int,sys.stdin.readline().split())

maps = []
dp = [[-1]*n for i in range(m)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]



def dfs(x,y):
    if x==m-1 and y==n-1:
        return 1
    if dp[x][y] ==-1:
        dp[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<m and 0<=ny<n and maps[nx][ny]<maps[x][y]:
                dp[x][y] += dfs(nx,ny)

    return dp[x][y]

for i in range(m):
    maps.append(list(map(int,sys.stdin.readline().split())))
print(dfs(0,0))