import sys

n, k = map(int, sys.stdin.readline().split())
l = []
stack = []
idx = 0

for i in range(1,n+1):
    l.append(i)


for i in range(n):
    idx += (k-1)

    if idx >= len(l):
        idx %= len(l)

    stack.append(str(l[idx]))
    l.pop(idx)


print("<",', '.join(stack),">", sep = "")
