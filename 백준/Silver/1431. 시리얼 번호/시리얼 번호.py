import sys


n = int(sys.stdin.readline())
numbers = []
for i in range(n):
    numbers.append(list(sys.stdin.readline().rstrip()))

def sum_num(s):
    result = 0
    for i in s:
        if i.isdigit():
            result+=int(i)
    return result

numbers.sort(key=lambda x:(len(x),sum_num(x),x))

for s in numbers:
    print(''.join(s))
