import sys

a = ' '+sys.stdin.readline().rstrip()
b = ' '+sys.stdin.readline().rstrip()

dp = [['']*len(b) for _ in range(len(a))]


for i in range(1,len(a)):
    for j in range(1,len(b)):
        if a[i] == b[j]:
            dp[i][j] = dp[i-1][j-1]+b[j]

        else:
            if len(dp[i-1][j]) >= len(dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]

rst = dp[-1][-1]
print(len(rst),rst,sep='\n')

