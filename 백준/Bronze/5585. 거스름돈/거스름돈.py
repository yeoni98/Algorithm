import sys

m = int(sys.stdin.readline())
n = 1000-m
lst = [500,100,50,10,5,1]
cnt = 0
for i in lst:
    cnt += n//i
    n %=i
print(cnt)