import sys


n = int(sys.stdin.readline())
pmt = list(map(int,sys.stdin.readline().split()))

dp = [[x for x in pmt] for _ in range(2)]


for i in range(1,n):
    dp[0][i] = max(dp[0][i-1]+pmt[i], dp[0][i])
    dp[1][i] = max(dp[0][i-1], dp[1][i-1]+pmt[i])

print(max(max(dp[0]),max(dp[1])))