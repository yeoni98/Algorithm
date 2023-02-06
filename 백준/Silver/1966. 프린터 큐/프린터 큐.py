import sys
from collections import deque

case = int(sys.stdin.readline())


for i in range(case):
    n, m = map(int,sys.stdin.readline().split())
    lst = deque(list(sys.stdin.readline().split()))
    idx = deque(list(range(n)))


    result = 0

    while lst:
        if lst[0] == max(lst):
            lst.popleft()
            result += 1
            pop_idx = idx.popleft()
         
            if pop_idx == m:
                print(result)




        else:
            lst.append(lst.popleft())
            idx.append(idx.popleft())
