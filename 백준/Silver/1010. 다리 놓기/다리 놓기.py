import sys

t = int(sys.stdin.readline())

def factorial(x):
    num = 1
    for i in range(1,x+1):
        num *= i
    return num

for y in range(t):
    w,e = map(int,input().split())
    result = factorial(e)//(factorial(e-w)*factorial(w))
    print(result)