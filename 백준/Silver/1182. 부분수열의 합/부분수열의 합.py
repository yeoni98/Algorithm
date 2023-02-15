from itertools import combinations
import sys

n, s = map(int,sys.stdin.readline().split())

lst = list(map(int,sys.stdin.readline().split()))
cnt = 0
for i in range(1,n+1):
    com = combinations(lst,i)

    for j in com:
        if sum(j) == s:
            cnt +=1
print(cnt)