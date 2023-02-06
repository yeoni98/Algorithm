import sys
from collections import deque

que = deque()
n = int(sys.stdin.readline())

for i in range(n):
    ord = sys.stdin.readline().split()

    if ord[0] == 'push':
        que.append(ord[1])
    if ord[0] == 'pop':
        if que:
            a = que.popleft()
            print(a)
        else:
            print(-1)
    if ord[0] == 'size':
        print(len(que))
    if ord[0] == 'empty':
        if que:
            print(0)
        else:
            print(1)
    if ord[0] == 'front':
        if que:
            print(que[0])
        else:
            print(-1)
    if ord[0] == 'back':
        if que:

            print(que[-1])
        else:
            print(-1)

