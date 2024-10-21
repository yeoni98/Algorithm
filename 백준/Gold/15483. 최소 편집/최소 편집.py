
import sys

l1 = sys.stdin.readline()
l2 = sys.stdin.readline()

n1 = len(l1)
n2 = len(l2)

dp = [[0]*(n2+1) for _ in range(n1+1)]

for i in range(n1+1):
    for j in range(n2+1):

        if i ==0:
            dp[i][j] = j

        elif j ==0:
            dp[i][j] = i

        else:
            if l1[i-1] == l2[j-1]:
                dp[i][j] = dp[i-1][j-1]

            else:
                dp[i][j] = 1+ min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])


print(dp[-1][-1])






