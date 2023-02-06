import sys
from collections import Counter


N = int(input())
A = list(map(int,input().split()))
M = int(input())
arr = list(map(int,input().split()))
count = Counter(A)

for i in range(len(arr)):
    if arr[i] in count:
        print(count[arr[i]])

    else:
        print(0)
