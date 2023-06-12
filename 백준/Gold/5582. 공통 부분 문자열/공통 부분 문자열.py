import sys

a = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()

dp = [[0]*(len(b)+1) for _ in range(len(a)+1)]

longest = 0

for i in range(1,len(a)+1):
    for j in range(1,len(b)+1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
            longest = max(longest,dp[i][j])

print(longest)