import sys

n = int(sys.stdin.readline())
h = list(map(int,sys.stdin.readline().split()))
ans = [0]*n

for i in range(n):
    cnt = 0

    for j in range(n):
        if cnt == h[i] and ans[j]==0:
            ans[j] = i+1
            break
        if ans[j] == 0:
            cnt += 1
print(*ans)
