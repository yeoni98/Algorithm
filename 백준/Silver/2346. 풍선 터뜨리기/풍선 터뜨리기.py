import sys
from collections import deque

n = int(sys.stdin.readline())
num = [i for i in range(1,n+1)]
result = []
numbers = list(map(int, input().split()))
idx = 0
tmp = numbers.pop(idx)
result.append(num.pop(idx))

while numbers:
    if tmp > 0:
        idx = (idx + tmp-1) % len(numbers)
    else:
        idx = (idx + tmp) % len(numbers)

    tmp = numbers.pop(idx)
    result.append(num.pop(idx))

print(*result, sep =' ')
