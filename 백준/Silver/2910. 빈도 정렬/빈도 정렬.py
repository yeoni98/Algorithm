import sys

n, c = map(int,sys.stdin.readline().split())

per = list(map(int,sys.stdin.readline().split()))

idx = 1
count = {}

for p in per:
    if p in count:
        count[p][0] += 1
    else:
        count[p] = [1,idx]
        idx +=1

numbers = [[i,j] for i,j in count.items()]
numbers.sort(key=lambda x:(-x[1][0], x[1][1]))
res = []

for i,j in numbers:
    res += [i]*j[0]

print(*res)

