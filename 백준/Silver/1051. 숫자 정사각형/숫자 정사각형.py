n, m = map(int, input().split())

sq = []

for i in range(n):
    sq.append(list(input()))

check = min(n, m)
ans = 0
for i in range(n):
    for j in range(m):
        for k in range(check):
            if ((i + k) < n) and ((j + k) < m) and (sq[i][j] == sq[i][j + k] == sq[i + k][j] == sq[i + k][j + k]):
                ans = max(ans, (k + 1)**2)
                
print(ans)