import sys

n = int(sys.stdin.readline())

cnt3 = 0
cnt5 = 0
while n > 0:
    if n % 5 == 0:
        cnt5 += n // 5
        n = 0
        break
    n -= 3
    cnt3 += 1

if n < 0:
    print(-1)
else:
    print(cnt3 + cnt5)