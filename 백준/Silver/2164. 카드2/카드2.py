import sys
from collections import deque

n = int(sys.stdin.readline())
que = deque()
for i in range(1,n+1):
    que.append(i)
while len(que)>1:
    que.popleft()
    que.append(que[0])
    que.popleft()

print(*que, sep = '')