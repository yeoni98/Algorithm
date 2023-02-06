import sys
import heapq

n = int(sys.stdin.readline())
h = []
for i in range(n):
    x = int(sys.stdin.readline().rstrip())

    if x != 0:
        heapq.heappush(h,(abs(x),x))
    else:
        if h:
            print(heapq.heappop(h)[1])
        else:
            print(0)
