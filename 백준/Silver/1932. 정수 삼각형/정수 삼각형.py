import sys

n = int(sys.stdin.readline())
tr = [[] for i in range(n)]
tr[0] = [int(sys.stdin.readline())]

for i in range(1,n):
    tr[i] = list(map(int,sys.stdin.readline().split()))

# print(tr)
# print(tr[0][0])
for i in range(1,n):
    for j in range(i+1):
        if j == 0:
            tr[i][j] += tr[i-1][j]
        elif j == i:
            tr[i][j] += tr[i-1][j-1]
        else:
            tr[i][j] += max(tr[i-1][j],tr[i-1][j-1])

print(max(tr[-1]))