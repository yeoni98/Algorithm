import sys
from itertools import combinations
n = int(sys.stdin.readline())
ss = []
bb = []
s_total = []
s_com = []
b_total = []
b_com = []
ans = []
for i in range(n):
    s, b = map(int,sys.stdin.readline().split())
    ss.append(s)
    bb.append(b)

com_list = []
for i in range(1,n+1):
    for s_total in combinations(ss,i):
        S = 1
        for j in s_total:
            S*=j
            s_com.append(S)

for i in range(1,n+1):
    for b_total in combinations(bb,i):
        B = 0
        for j in b_total:
            B += j
            b_com.append(B)
            
for i in range(len(s_com)):
    ans.append(abs(s_com[i]-b_com[i]))

print(min(ans))
