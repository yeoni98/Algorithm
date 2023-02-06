import sys

n = list(input())
m = int(input())
stack = []


for i in range(m):
    a = sys.stdin.readline().split()
    if a[0] == "L" and n:
        stack.append(n.pop())
    elif a[0] == "D" and stack:
        n.append(stack.pop())
    elif a[0] == "B" and n:
        n.pop()
    elif a[0] == "P":
        n.append(a[1])


print("".join(n+list(reversed(stack))))