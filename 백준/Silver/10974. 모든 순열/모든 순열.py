import sys
import itertools

n = int(sys.stdin.readline())
num = []
for i in range(1,n+1):
    num.append(i)

ans = itertools.permutations(num, n)

for i in ans:
    print(*i)
