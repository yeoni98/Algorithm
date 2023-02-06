import sys

N, K = map(int, input().split())
lst = list()
for n in range(N):
    a = int(input())
    lst.append(a)

lst.sort(reverse=True)
result = 0
for i in lst:
    if K >= i:
        result += K // i
        K %= i
        if K <= 0:
            break

print(result)

