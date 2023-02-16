import sys
n, m = map(int,sys.stdin.readline().split())
data = list(map(int,sys.stdin.readline().split()))

cnt = 0
j = 0
for i in range(n):
    tmp = 0
    for j in range(i,n):
        tmp +=data[j]
        if tmp == m:
            cnt += 1
            break
        if tmp > m:
            break
print(cnt)