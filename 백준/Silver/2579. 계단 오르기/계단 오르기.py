import sys

t = int(input())
s = [int(input()) for i in range(t)]
dp = [0]*(t+1)
if t<=2:
    print(sum(s))
else:
    dp[0]=s[0]
    dp[1]=s[0]+s[1]
    

    for i in range(2,t):
        dp[i]=max(dp[i-2]+s[i], dp[i-3]+s[i-1]+s[i])
    print(dp[i])