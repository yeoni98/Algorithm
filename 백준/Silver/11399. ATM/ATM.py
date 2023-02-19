import sys

n = int(sys.stdin.readline())
needed_time = list(map(int,sys.stdin.readline().split()))

needed_time.sort()
min_time = 0

for i in range(1,n+1):
    min_time += sum(needed_time[:i])

print(min_time)