import sys
from collections import deque

n, m = map(int,sys.stdin.readline().split())

lst = list(map(int,sys.stdin.readline().split()))

q = deque([i for i in range(1,n+1)])

cnt = 0

for l in lst:
    while 1:
        if q[0] == l:
            q.popleft()
            break
        else:
            if q.index(l) <= len(q)//2:
                q.rotate(-1)
                cnt +=1
            else:
                q.rotate(1)
                cnt +=1

print(cnt)
