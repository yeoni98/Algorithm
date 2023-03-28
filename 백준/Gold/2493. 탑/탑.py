import sys

n = int(sys.stdin.readline())
top = list(map(int,sys.stdin.readline().split()))
ans = []
stack = []


for i in range(n):
    while stack:
        if stack[-1][1]>top[i]:
            ans.append(stack[-1][0]+1)
            break
        else:
            stack.pop()
    if not stack:
        ans.append(0)

    stack.append((i,top[i]))

print(*ans)
