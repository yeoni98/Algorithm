import sys

n = int(input())

for i in range(n):
    tmp = list(sys.stdin.readline().rstrip())
    stack = []
    pswd = []
    
    for j in tmp:
        if j == '<':
            if pswd:
                stack.append(pswd.pop())
        elif j == '>':
            if stack:
                pswd.append(stack.pop())

        elif j == '-':
            if pswd:
                pswd.pop()
        else:
            pswd.append(j)

    print("".join(pswd),"".join(stack[::-1]),sep="")