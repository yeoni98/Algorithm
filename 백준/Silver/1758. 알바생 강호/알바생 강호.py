import sys

n = int(sys.stdin.readline())
a = []
tip = 0
for i in range(n):
    a.append(int(sys.stdin.readline()))
a.sort(reverse=True)
for i in range(n):
    x = a[i] - i
    if x > 0:
        tip += x

print(tip)
