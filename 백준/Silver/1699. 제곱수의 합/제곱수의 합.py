import sys
import math
# 참고!
# 16+25 =41이지만 본문의 코드는 3을 출력하네요.
#
# 아마 25대신 36부터 넣어서 36+4+1을 만든 거 같아요.
#
# 무조건 큰 제곱수부터 빼는 것이 정답이 아닙니다.
n = int(sys.stdin.readline())

dp = [_ for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1, int(math.sqrt(i)+1)):
        if dp[i]>dp[i-j*j]+1:
            dp[i] = dp[i-j*j]+1

print(dp[n])
#dp[1] = 1, dp[2] = 2, dp[3]  =3
#dp[4]= 2, dp[3] =
#dp[5] = 2, dp[6] = 3 dp[7] = 4




# 틀린 답
# cnt = 0
#
# while n>0:
#     m = int(math.sqrt(n))
#     print(m)
#     if m == 1:
#         n -= 1
#     else:
#         n -= m**2
#
#     print(n)
#     cnt +=1
#
#
# print(cnt)
#
