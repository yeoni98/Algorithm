import sys

n, k = list(map(int,sys.stdin.readline().split()))

diff = []
lst = list(map(int,sys.stdin.readline().split()))

for i in range(n-1):
    diff.append(lst[i+1]-lst[i])

diff.sort()
result = 0
print(sum(diff[:n-k]))
