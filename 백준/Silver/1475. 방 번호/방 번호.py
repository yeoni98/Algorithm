import sys
import math


num = ['0','1','2','3','4','5','6','7','8','9']
result = [0]*10
sixnine = []
n = list(input())

for i in range(len(n)):
    if n[i] in num:
        result[num.index(n[i])] +=1

sixnine.extend([n.count('6'),n.count('9')])


result[6] = math.ceil(sum(sixnine)/2)
result[9] = math.ceil(sum(sixnine)/2)


print(max(result))