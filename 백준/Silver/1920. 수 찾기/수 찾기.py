import sys
N = int(input())
A = set(map(int,input().split()))
M = int(input())
arr = list(map(int,input().split()))

for i in arr:
    if i in A:
        print(1)
    else:
        print(0)

