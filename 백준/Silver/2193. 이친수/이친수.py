import sys

n = int(sys.stdin.readline())
d = [0]*91
d[0] = 0
d[1] = 1
d[2] = 1


for i in range(3,91):
    d[i] = d[i-2] + d[i-1]

print(d[n])
