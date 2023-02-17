import sys

m, n = map(int, sys.stdin.readline().split())
dict = {}
ans = []
for i in range(m):
    add, pswd = sys.stdin.readline().split()
    dict[add] = pswd

for i in range(n):
    ans = sys.stdin.readline().rstrip()
    print(dict[ans])