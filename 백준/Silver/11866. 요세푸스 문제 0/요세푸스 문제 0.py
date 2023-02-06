import sys


n, k = list(map(int,sys.stdin.readline().split()))
circle = []
que = []
ord = 0
for i in range(1,n+1):
    circle.append(i)

while circle:
    ord += k

    if len(circle) >= ord:
        ord -= 1
        que.append(circle.pop(ord))
        if ord < 0:
            ord = 0
    else:
        if len(circle) == 1:
            que.append(circle.pop(0))
        else:
            ord %= len(circle)
            ord -= 1
            que.append(circle.pop(ord))
            if ord < 0:
                ord = 0



print("<",", ".join(map(str,que)), ">", sep="")

# 1 2 3 4 5 6 7
# 1 2 4 5 6 7       3                i = 2
# 1 2 4 5 7         3 6              i = 2+3-1 = 4
# 1 4 5 7           3 6 2            i = (4+3)/5 -1 = 1
# 1 4 5             3 6 2 7          i = 1+3 -1 = 3
# 1 4               3 6 2 7 5        i = (3+3)/3 -1  = -1
# 4                 3 6 2 7 5 1      i = (-1+3)/2 = 0