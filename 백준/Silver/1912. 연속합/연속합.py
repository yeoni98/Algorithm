import sys

n = int(sys.stdin.readline())
dp = [0]*n
l = list(map(int,sys.stdin.readline().split()))
# start = 0
# max_num = min(l)
for i in range (1,n):
    # print(sum(l[start:i]))
    # print(max_num)
    # print()
    # if sum(l[start:i]) > max_num:
    #     dp[i] = sum(l[start:i])
    #
    #     max_num = sum(l[start:i])
    #     i +=1
    #
    # else:
    #     start +=1
    #     i+=1
    l[i] = max(l[i], l[i-1]+l[i])


print(max(l))
