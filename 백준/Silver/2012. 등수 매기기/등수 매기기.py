import sys


n = int(sys.stdin.readline())
num = []
for i in range(n):
    num.append(int(sys.stdin.readline()))

num.sort()
difference = 0
for i in range(1,len(num)+1):
    difference += abs(num[i-1]-i)

print(difference)

