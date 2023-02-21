import sys
import itertools

n = int(sys.stdin.readline())
num = list(map(int,sys.stdin.readline().split()))

if n == 1:
    print(-1)
else:
    idx = n
    for i in range(n-2,-1,-1):
        if num[i] > num[i+1]:
            idx = i
            break
    if idx == n:
        print(-1)
    else:
        idx2 = n
        for i in range(n-1,-1,-1):
            if num[idx] > num[i]:
                num[idx],num[i] = num[i], num[idx]
                break
        num = num[:idx+1]+sorted(num[idx+1:],reverse = True)
        print(*num)

