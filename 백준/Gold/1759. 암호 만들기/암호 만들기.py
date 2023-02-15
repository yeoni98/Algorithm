from itertools import combinations
import sys

l, c = map(int,sys.stdin.readline().split())
alpha = list(sys.stdin.readline().split())
sorted_alpha = sorted(alpha)
aeiou = ['a','e','i','o','u']
com = []
cnt = 0

for i in combinations(sorted_alpha,l):
    com.append(i)

for i in com:
    cnt = 0
    for j in aeiou:
        if j in i:
            cnt +=1
    if 0<cnt and l-cnt>1:
        print(''.join(i))