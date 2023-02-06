import sys
import math
from collections import Counter

n = int(sys.stdin.readline())

lst = []

for i in range(n):
    x = int(sys.stdin.readline())
    lst.append(x)
lst.sort()
average = sum(lst)/n
middle = lst[int(n/2)]
cnt = Counter(lst)
most = cnt.most_common(2)
max_min = max(lst)-min(lst)



print(round(average))
print(middle)
if len(lst) > 1:
    if most[0][1] == most[1][1]:
        print(most[1][0])
    else:
        print(most[0][0])

else:
    print(most[0][0])

print(max_min)