import sys

n = int(sys.stdin.readline())
dp = [0]*(n+1)
dp[0] = 1

if n>=2:
    dp[2] = 3
for i in range(4, n+1, 2):
    dp[i] = dp[i-2]*dp[2]
    for j in range(0,i-2, 2):
        dp[i] += dp[j]*2

print(dp[n])
