import sys

n, m = map(int,sys.stdin.readline().split())
s = set()
result = 0
for i in range(n):
    s.add(sys.stdin.readline().rstrip())

for i in range(m):
    t = sys.stdin.readline().rstrip()
    if t in s:
        result +=1

print(result)