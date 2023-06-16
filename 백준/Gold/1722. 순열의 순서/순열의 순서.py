import sys

n = int(sys.stdin.readline())
input = list(map(int,sys.stdin.readline().split(' ')))
num = []

def factorial(inp):
    if inp<=1:
        return 1
    else:
        return inp * factorial(inp-1)


for i in range(1,n+1):
    num.append(i)

if input[0] == 1:
    ord = input[1]
    temp = []

    for i in range(n,0,-1):
        fac = factorial(i-1)
        step = (ord-1)//fac
        temp.append(num[step])
        num.remove(num[step])
        ord -= step*fac
    print(*temp)

else:
    lst = input[1:]
    ord = 1
    for i in range(n,0,-1):
        fac = factorial(i-1)
        step = num.index(lst[n-i])
        num.remove(num[step])
        ord += fac*step
    print(ord)
