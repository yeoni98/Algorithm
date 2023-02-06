import sys

n, k = map(int,sys.stdin.readline().split())
d = [[0]*(k+1) for i in range(n+1)]

for i in range(1,n+1):
    w, v = map(int,sys.stdin.readline().split())
    for j in range(1,k+1):
        if j < w:
            d[i][j] = d[i-1][j]
        else:
            d[i][j] = max(d[i-1][j],d[i-1][j-w]+v)


print(d[n][k])