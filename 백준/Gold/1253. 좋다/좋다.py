import sys

n = int(sys.stdin.readline())
num = sorted(list(map(int,sys.stdin.readline().split())))
cnt = 0

for i in range(n):
    lst = num[:i] + num[i+1:]
    start, end = 0, len(lst) -1

    while start<end:
        total = lst[start]+lst[end]
        if total == num[i]:
            cnt += 1
            break
        if total < num[i]:
            start += 1
        else:
            end -= 1
print(cnt)
