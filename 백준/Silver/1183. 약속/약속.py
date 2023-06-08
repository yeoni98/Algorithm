import sys

n = int(sys.stdin.readline())
l = []

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    l.append(b-a)
l.sort()
if n %2 == 1:
    print(1)
if n%2 == 0:
    i = n//2
    print(l[i]-l[i-1]+1)
