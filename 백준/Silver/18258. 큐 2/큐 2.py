import sys
from collections import deque

n = int(sys.stdin.readline())
que = deque()

for i in range(n):
    a = sys.stdin.readline().split()

    if a[0] == 'push':
        que.append(a[1])
    if a[0] == 'pop':
        if que:
            print(que[0])
            que.popleft()
        else:
            print('-1')
    if a[0] == 'size':
        print(len(que))
    if a[0] == 'empty':
        if que:
            print('0')
        else:
            print('1')
    if a[0] == 'front':
        if que:
            print(que[0])
        else:
            print('-1')
    if a[0] == 'back':
        if que:
            print(que[-1])
        else:
            print('-1')

