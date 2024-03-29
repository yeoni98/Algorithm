import sys

a = list(sys.stdin.readline().rstrip())
b = list(sys.stdin.readline().rstrip())

dp = [[0]*(len(b)+1) for _ in range(len(a)+1)]

for i in range(1,len(a)+1):
    for j in range(1,len(b)+1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1] +1
            
        else:                # 왼쪽     ,     위
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])
            


print(dp[-1][-1])