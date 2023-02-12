import sys

n, k = map(int,sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
cnt = 0
ans = -1

for i in range(n-1,0,-1):
    for j in range(i):
        if a[j] > a[j+1]:
            cnt += 1
            a[j], a[j+1] = a[j+1], a[j]

            if cnt == k:
                print(a[j], a[j+1])

if cnt < k:
    print(-1)