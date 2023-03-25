import sys

n, m = map(int,sys.stdin.readline().split())
lst = list(map(int,sys.stdin.readline().split()))
plus = []
minus = []
ans = 0
for i in lst:
    if i<0:
        minus.append(i*(-1))
    else:
        plus.append(i)
minus.sort(reverse=True)
plus.sort(reverse=True)
l = []

for i in range(len(minus)//m):
    l.append(minus[i*m])
if len(minus)%m >0:
    l.append(minus[(len(minus)//m)*m])

for i in range(len(plus)//m):
    l.append(plus[i*m])
if len(plus)%m>0:
    l.append(plus[(len(plus)//m)*m])



l.sort()
max_num =l.pop()
ans = 2*sum(l)+max_num

print(ans)

# -6 -28 -29 -37 -39
# 2 11
#
# -4 -9 -18 22 -26 40 -45 50
#
# -4 -9 -18 -26 -45
# 22 40 50
#
# 50+90+18
#
# 3 4 5 6 11
# -1
# 11+10+6+2 = 29
