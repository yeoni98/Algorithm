import sys

n = int(sys.stdin.readline())
s = list(sys.stdin.readline().rstrip())
num = [0]*n

for i in range(n):
    num[i] = int(input())

stack = []

for i in range(len(s)):
    if 'A'<=s[i]<='Z':
        stack.append(num[ord(s[i]) - ord('A')])

    else:
        str2 = stack.pop()
        str1 = stack.pop()
        if s[i] == '*':
            stack.append(str1 * str2)

        elif s[i] == '+':
            stack.append(str1 + str2)

        elif s[i] == '/':
            stack.append(str1 / str2)

        elif s[i] == '-':
            stack.append(str1 - str2)



print('%.2f'%stack[0])