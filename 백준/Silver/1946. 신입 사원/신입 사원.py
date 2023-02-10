import sys

t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())
    a = []
    for j in range(n):
        a.append(list(map(int,sys.stdin.readline().split())))
    sorted_a = sorted(a, key = lambda x:x[0])
    cnt = 1

    score = sorted_a[0][1]

    for j in range(1,n):
        if sorted_a[j][1] < score:
            score = sorted_a[j][1]
            cnt += 1

    print(cnt)