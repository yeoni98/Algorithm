import sys

h, w = map(int, sys.stdin.readline().split())
block = list(map(int,sys.stdin.readline().split()))
ans = 0

for i in range(1, w-1):
    left = max(block[:i])
    right = max(block[i+1:])
    m = min(left,right)

    if m > block[i]:
        ans += (m-block[i])
print(ans)

