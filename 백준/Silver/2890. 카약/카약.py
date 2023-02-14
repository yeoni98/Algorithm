import re
import sys

r,c = map(int,sys.stdin.readline().split())

lst = [-1]*9

for i in range(r):
    s = re.split('[1-9]{2}',sys.stdin.readline())
    if s[0].count('.')!= c-2:
        lst[int(s[1][0])-1] = ((c-5)-s[0].count('.'))

ans = []
set_lst = set(lst)
ord = sorted(list(set_lst))

for i in lst:
    ans.append(ord.index(i)+1)

print(*ans, sep='\n')