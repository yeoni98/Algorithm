import sys
from collections import deque

t = int(sys.stdin.readline())

for i in range(t):
    que = deque()
    p = list(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline())
    lst = input()[1:-1].split(',')
    que = deque(lst)


    flag = 0

    if n == 0:
        que = []

    for i in p:
        if i == 'R':
            flag +=1
        if i == 'D':
            if len(que) == 0:
                print('error')
                break
            else:
                if flag%2==0:
                    que.popleft()
                else:
                    que.pop()

    else:
        if flag %2==1:
            que.reverse()
        print('['+','.join(que)+']')

