import sys
K, N = map(int,input().split())
n = [int(input()) for x in range(K)]

def Binary(target, start, end):
    if start>end:
        print(end)
        return

    mid = (start + end)//2
    line = 0
    for i in n:
        tmp = i//mid
        line += tmp

    if line < target:
        return Binary(target, start, mid-1)
    else:
        return Binary(target, mid+1, end)

Binary(N, 1, max(n))
