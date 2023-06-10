import sys


a = ' '+sys.stdin.readline().rstrip()
b = ' '+sys.stdin.readline().rstrip()
c = ' '+sys.stdin.readline().rstrip()

dp = [[[0]*len(c) for i in range(len(b))] for j in range(len(a))]

for i in range(1,len(a)):
    for j in range(1,len(b)):
        for k in range(1,len(c)):
            if a[i] == b[j] == c[k]:
                dp[i][j][k] = dp[i-1][j-1][k-1]+1
            else:
                dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1], dp[i-1][j-1][k], dp[i-1][j][k-1],dp[i][j-1][k-1])


print(dp[-1][-1][-1])
