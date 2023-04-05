import sys
from collections import deque

def solution(n, m, section):
    answer = 0
    q = deque(section)
    while q:
        x = q.popleft()
        while q and x+m > q[0]:
            q.popleft()
        answer +=1
  
    return answer


# n = int(sys.stdin.readline())
# m = int(sys.stdin.readline())
# selection = list(map(int,sys.stdin.readline().split()))

