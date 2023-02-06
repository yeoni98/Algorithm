import sys

n = int(sys.stdin.readline())

dp = [[0]*10 for i in range(n)]

dp[0] = [0,1,1,1,1,1,1,1,1,1]

for i in range(1,n):
    dp[i][0] = dp[i-1][1] #처음
    dp[i][9] = dp[i-1][8] #끝

    for j in range(1,9):
        dp[i][j] = dp[i-1][j-1]+dp[i-1][j+1]

print(sum(dp[n-1])%1000000000)