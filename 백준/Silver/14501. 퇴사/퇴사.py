import sys


n = int(sys.stdin.readline())
sch = []
dp = [0]*(n+1)
for i in range(n):
    days, pay = map(int,sys.stdin.readline().split())
    sch.append((days, pay))

for i in range(n-1,-1,-1):
    if i+sch[i][0]>n:
        dp[i] = dp[i+1] # 복사
    else:
        dp[i] = max(sch[i][1] + dp[i+sch[i][0]],dp[i+1])

print(dp[0])