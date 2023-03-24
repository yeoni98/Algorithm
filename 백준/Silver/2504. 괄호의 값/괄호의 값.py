import sys

lst = list(sys.stdin.readline().rstrip())
lens = len(lst)
ans = 0
tmp = 1
stack = []
for i in range(lens):
    a = lst[i]
    if a == '(':
        tmp *= 2
        stack.append(a)
    elif a == '[':
        tmp*=3
        stack.append(a)
    elif a == ')':
        if not stack or stack[-1] == '[':
            ans = 0
            break
        if lst[i-1] == '(':
            ans += tmp
        stack.pop()
        tmp//=2

    elif a == "]":
        if not stack or stack[-1] == '(':
            ans = 0
            break
        if lst[i-1] == '[':
            ans += tmp
        stack.pop()
        tmp //=3
if stack:
    print(0)
else:
    print(ans)



