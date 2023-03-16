import sys
from collections import deque

a, b = map(int,sys.stdin.readline().split())

que = deque([(1,a)])

while que:
    cnt, x = que.popleft()

    if x == b:
        print(cnt)
        break

    if x*2 <= b:
        que.append((cnt+1, x*2))
    if x*10+1 <=b:
        que.append((cnt+1, x*10+1))
else:
    print(-1)