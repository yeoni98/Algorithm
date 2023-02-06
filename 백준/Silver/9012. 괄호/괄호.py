import sys

n = int(sys.stdin.readline())

for i in range(n):
    a = str(input())
    stack=[]
    for j in a:



        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack:
                stack.pop()
            else:
                print('NO')
                break

    else:
        if stack:
            print('NO')
        else:
            print('YES')
