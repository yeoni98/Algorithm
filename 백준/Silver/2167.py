import sys

n, m = map(int,sys.stdin.readline().split())
lst = []
result = []

for i in range(n):
    lst.append(list(map(int, input().split())))

k = int(input())

for i in range(k):
    i,j,x,y = map(int,input().split())
    result.append(sum(lst[i-1][j-1::])-sum(lst[x-1][y::]))
    print(result)