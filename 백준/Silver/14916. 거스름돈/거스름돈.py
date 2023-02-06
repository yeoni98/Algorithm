import sys

coin = [5,2]
not_ = [1,3]
n = int(sys.stdin.readline())


if n in not_:
    print(-1)
elif n%5== 0:
    print(n//5)
elif n%5%2 == 0:
    print(n//5 + n%5//2)
else:
    print((n-5)//5 + ((n-5)%5+5)//2)