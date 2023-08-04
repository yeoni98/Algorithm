
import sys

t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())
    numb = []
    flag = 'YES'
    for j in range(n):
        numb.append(sys.stdin.readline().rstrip())
    numb.sort()
    for j in range(n-1):
        if numb[j] == numb[j+1][:len(numb[j])]:
            flag = 'NO'
            break
    print(flag)
