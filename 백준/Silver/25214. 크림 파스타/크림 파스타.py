import sys

n = int(sys.stdin.readline())

a = list(map(int,sys.stdin.readline().split()))
d = [0]*n
min_ = a[0]

for i in range(1, n):
    min_ = min(min_,a[i])
    d[i] = (max(d[i-1],a[i]-min_))
print(*d)